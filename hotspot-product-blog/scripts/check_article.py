#!/usr/bin/env python3
"""Static HTML sanity check, not a semantic or publication quality score."""
import argparse
import json
from html.parser import HTMLParser
from pathlib import Path
from collections import Counter


class Scan(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.anchors, self.images, self.ctas = [], [], [], []
        self.h1 = self.h2 = self.nav = 0
        self.title = self.viewport = False
        self.text = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ('style', 'script'):
            self.hidden += 1
        if a.get('id'):
            self.ids.append(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'h2': self.h2 += 1
        if tag == 'nav': self.nav += 1
        if tag == 'title': self.title = True
        if tag == 'meta' and a.get('name') == 'viewport': self.viewport = True
        if tag == 'img': self.images.append(a)
        if tag == 'a':
            href = a.get('href', '')
            if href.startswith('#'): self.anchors.append(href[1:])
            if 'cta' in a.get('class', '').split(): self.ctas.append(href)

    def handle_endtag(self, tag):
        if tag in ('style', 'script') and self.hidden:
            self.hidden -= 1

    def handle_data(self, data):
        if not self.hidden: self.text.append(data)


def check(html):
    s = Scan()
    s.feed(html)
    errors, warnings = [], []
    if s.h1 != 1: errors.append('Expected exactly one H1')
    if not s.title: errors.append('Missing title')
    if not s.viewport: errors.append('Missing viewport metadata')
    duplicate = [k for k, n in Counter(s.ids).items() if n > 1]
    if duplicate: errors.append('Duplicate IDs: ' + ', '.join(duplicate))
    broken = [x for x in s.anchors if x not in s.ids]
    if broken: errors.append('Broken anchors: ' + ', '.join(broken))
    if any(not i.get('alt', '').strip() or not i.get('src', '').strip() for i in s.images):
        errors.append('Image missing alt or src')
    if any(not x.startswith('https://') for x in s.ctas):
        errors.append('Product CTA must link to a real HTTPS product URL')
    visible = ' '.join(s.text).lower()
    if 'editorial image placeholder' in visible or '{{' in visible or '}}' in visible:
        errors.append('Visible placeholder or template variable')
    if s.h2 > 1 and not (s.nav and s.anchors): warnings.append('Check section navigation')
    if not s.images: warnings.append('No images; explain if visual support is unavailable or unnecessary')
    if not s.ctas: warnings.append('No product CTA; verify product-pending status or intended layout')
    return {'errors': errors, 'warnings': warnings,
            'counts': {'h1': s.h1, 'h2': s.h2, 'images': len(s.images), 'ctas': len(s.ctas)},
            'scope': 'Static structure only; facts, remote assets, rendering and publication remain unverified'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('html', type=Path)
    args = parser.parse_args()
    result = check(args.html.read_text(encoding='utf-8'))
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(1 if result['errors'] else 0)
