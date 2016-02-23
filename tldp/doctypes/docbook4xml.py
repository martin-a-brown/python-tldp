#! /usr/bin/python
# -*- coding: utf8 -*-

from ..utils import logger, which, firstfoundfile
from .common import SignatureChecker

def xslchunk_finder():
    l = ['/usr/share/xml/docbook/stylesheet/ldp/html/tldp-sections.xsl',
         ]
    return firstfoundfile(l)


def xslsingle_finder():
    l = ['/usr/share/xml/docbook/stylesheet/ldp/html/tldp-one-page.xsl',
         ]
    return firstfoundfile(l)


def xslprint_finder():
    l = ['/usr/share/xml/docbook/stylesheet/ldp/fo/tldp-print.xsl',
         ]
    return firstfoundfile(l)


def config_fragment(p):
    p.add_argument('--docbook4xml-xslchunk', type=str,
                   default=xslchunk_finder(),
                   help='full path to LDP HTML section chunker XSL [%(default)s]')
    p.add_argument('--docbook4xml-xslsingle', type=str,
                   default=xslsingle_finder(),
                   help='full path to LDP HTML single-page XSL [%(default)s]')
    p.add_argument('--docbook4xml-xslprint', type=str,
                   default=xslprint_finder(),
                   help='full path to LDP FO print XSL [%(default)s]')
    p.add_argument('--docbook4xml-xsltproc', type=which,
                   default=which('xsltproc'),
                   help='full path to xsltproc [%(default)s]')
    p.add_argument('--docbook4xml-html2text', type=which,
                   default=which('html2text'),
                   help='full path to html2text [%(default)s]')
    p.add_argument('--docbook4xml-fop', type=which,
                   default=which('fop'),
                   help='full path to fop [%(default)s]')
    p.add_argument('--docbook4xml-dblatex', type=which,
                   default=which('dblatex'),
                   help='full path to dblatex [%(default)s]')


class Docbook4XML(SignatureChecker):
    formatname = 'DocBook XML 4.x'
    extensions = ['.xml']
    signatures = ['-//OASIS//DTD DocBook XML V4.1.2//EN',
                  '-//OASIS//DTD DocBook XML V4.2//EN',
                  '-//OASIS//DTD DocBook XML V4.2//EN',
                  '-//OASIS//DTD DocBook XML V4.4//EN',
                  '-//OASIS//DTD DocBook XML V4.5//EN', ]
    tools = ['xsltproc', 'html2text', 'fop', 'dblatex']
    files = ['']

    def create_txt(self):
        logger.info("Creating txt for %s", self.source.stem)

    def create_pdf(self):
        logger.info("Creating PDF for %s", self.source.stem)

    def create_html(self):
        logger.info("Creating chunked HTML for %s", self.source.stem)

    def create_htmls(self):
        logger.info("Creating single page HTML for %s", self.source.stem)

#
# -- end of file
