# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/11_xml.ipynb.

# %% auto 0
__all__ = ['voids', 'FT', 'ft', 'Html', 'to_xml', 'highlight', 'showtags', 'Head', 'Title', 'Meta', 'Link', 'Style', 'Body',
           'Pre', 'Code', 'Div', 'Span', 'P', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Strong', 'Em', 'B', 'I', 'U', 'S',
           'Strike', 'Sub', 'Sup', 'Hr', 'Br', 'Img', 'A', 'Nav', 'Ul', 'Ol', 'Li', 'Dl', 'Dt', 'Dd', 'Table', 'Thead',
           'Tbody', 'Tfoot', 'Tr', 'Th', 'Td', 'Caption', 'Col', 'Colgroup', 'Form', 'Input', 'Textarea', 'Button',
           'Select', 'Option', 'Label', 'Fieldset', 'Legend', 'Details', 'Summary', 'Main', 'Header', 'Footer',
           'Section', 'Article', 'Aside', 'Figure', 'Figcaption', 'Mark', 'Small', 'Iframe', 'Object', 'Embed', 'Param',
           'Video', 'Audio', 'Source', 'Canvas', 'Svg', 'Math', 'Script', 'Noscript', 'Template', 'Slot']

# %% ../nbs/11_xml.ipynb
from .utils import *

import types,json

from dataclasses import dataclass, asdict
from typing import Mapping
from functools import partial
from html import escape

# %% ../nbs/11_xml.ipynb
def _attrmap(o):
    o = dict(htmlClass='class', cls='class', _class='class', klass='class',
             _for='for', fr='for', htmlFor='for').get(o, o)
    return o.lstrip('_').replace('_', '-')

# %% ../nbs/11_xml.ipynb
class FT(list):
    "A 'Fast Tag' structure, which is a `list` of `[tag,children,attrs]`"
    def __init__(self, tag, cs, attrs=None, void_=False, **kwargs):
        super().__init__([tag, cs, {**(attrs or {}), **kwargs}])
        self.void_ = void_

    @property
    def tag(self): return self[0]
    @property
    def children(self): return self[1]
    @property
    def attrs(self): return self[2]

    def __setattr__(self, k, v):
        if k.startswith('__') or k in ('tag','cs','attrs','void_'): return super().__setattr__(k,v)
        self.attrs[k.lstrip('_').replace('_', '-')] = v

    def __getattr__(self, k):
        if k.startswith('__') or k not in self.attrs: raise AttributeError(k)
        return self.attrs[k.lstrip('_').replace('_', '-')]

# %% ../nbs/11_xml.ipynb
def _preproc(c, kw):
    if len(c)==1 and isinstance(c[0], (types.GeneratorType, map, filter)): c = tuple(c[0])
    return c,{_attrmap(k):v for k,v in kw.items() if v is not None}

# %% ../nbs/11_xml.ipynb
def ft(tag:str, *c, void_=False, **kw):
    "Create an `FT` structure for `to_xml()`"
    return FT(tag.lower(),*_preproc(c,kw), void_=void_)

# %% ../nbs/11_xml.ipynb
voids = set('area base br col command embed hr img input keygen link meta param source track wbr !doctype'.split())
_g = globals()
_all_ = ['Head', 'Title', 'Meta', 'Link', 'Style', 'Body', 'Pre', 'Code',
    'Div', 'Span', 'P', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'Strong', 'Em', 'B',
    'I', 'U', 'S', 'Strike', 'Sub', 'Sup', 'Hr', 'Br', 'Img', 'A', 'Link', 'Nav',
    'Ul', 'Ol', 'Li', 'Dl', 'Dt', 'Dd', 'Table', 'Thead', 'Tbody', 'Tfoot', 'Tr',
    'Th', 'Td', 'Caption', 'Col', 'Colgroup', 'Form', 'Input', 'Textarea',
    'Button', 'Select', 'Option', 'Label', 'Fieldset', 'Legend', 'Details',
    'Summary', 'Main', 'Header', 'Footer', 'Section', 'Article', 'Aside', 'Figure',
    'Figcaption', 'Mark', 'Small', 'Iframe', 'Object', 'Embed', 'Param', 'Video',
    'Audio', 'Source', 'Canvas', 'Svg', 'Math', 'Script', 'Noscript', 'Template', 'Slot']

for o in _all_: _g[o] = partial(ft, o.lower(), void_=o.lower() in voids)

# %% ../nbs/11_xml.ipynb
def Html(*c, doctype=True, **kwargs)->FT:
    "An HTML tag, optionally preceeded by `!DOCTYPE HTML`"
    res = ft('html', *c, **kwargs)
    if not doctype: return res
    return (ft('!DOCTYPE', html=True, void_=True), res)

# %% ../nbs/11_xml.ipynb
def _escape(s): return '' if s is None else s.__html__() if hasattr(s, '__html__') else escape(s) if isinstance(s, str) else s

# %% ../nbs/11_xml.ipynb
def _to_attr(k,v):
    if isinstance(v,bool):
        if v==True : return str(k)
        if v==False: return ''
    if isinstance(v,str): v = escape(v, quote=True)
    elif isinstance(v, Mapping): v = json.dumps(v)
    else: v = str(v)
    qt = '"'
    if qt in v: qt = "'"
    return f'{k}={qt}{v}{qt}'

# %% ../nbs/11_xml.ipynb
def to_xml(elm, lvl=0):
    "Convert `ft` element tree into an XML string"
    if elm is None: return ''
    if isinstance(elm, tuple): return '\n'.join(to_xml(o) for o in elm)
    if hasattr(elm, '__ft__'): elm = elm.__ft__()
    sp = ' ' * lvl
    if not isinstance(elm, list): return f'{_escape(elm)}\n'

    tag,cs,attrs = elm
    stag = tag
    if attrs:
        sattrs = (_to_attr(k,v) for k,v in attrs.items())
        stag += ' ' + ' '.join(sattrs)

    isvoid = getattr(elm, 'void_', False)
    cltag = '' if isvoid else f'</{tag}>'
    if not cs: return f'{sp}<{stag}>{cltag}\n'
    if len(cs)==1 and not isinstance(cs[0],(list,tuple)) and not hasattr(cs[0],'__ft__'):
        return f'{sp}<{stag}>{_escape(cs[0])}{cltag}\n'
    res = f'{sp}<{stag}>\n'
    res += ''.join(to_xml(c, lvl=lvl+2) for c in cs)
    if not isvoid: res += f'{sp}{cltag}\n'
    return res

FT.__html__ = to_xml

# %% ../nbs/11_xml.ipynb
def highlight(s, lang='html'):
    "Markdown to syntax-highlight `s` in language `lang`"
    return f'```{lang}\n{to_xml(s)}\n```'

# %% ../nbs/11_xml.ipynb
def showtags(s):
    return f"""<code><pre>
{escape(to_xml(s))}
</code></pre>"""

FT._repr_markdown_ = highlight

# %% ../nbs/11_xml.ipynb
def __getattr__(tag):
    if tag.startswith('_') or tag[0].islower(): raise AttributeError
    def _f(*c, target_id=None, **kwargs): return ft(tag, *c, target_id=target_id, **kwargs)
    return _f

# %% ../nbs/11_xml.ipynb
@patch
def __call__(self:FT, *c, **kw):
    c,kw = _preproc(c,kw)
    if c: self[1] = self[1]+c
    if kw: self[2] = {**self[2], **kw}
    return self
