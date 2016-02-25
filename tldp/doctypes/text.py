#! /usr/bin/python
# -*- coding: utf8 -*-

from __future__ import absolute_import, division, print_function

import logging
logger = logging.getLogger()

from tldp.doctypes.common import BaseDoctype


class Text(BaseDoctype):
    formatname = 'plain text'
    extensions = ['.txt']
    signatures = []
    tools = ['pandoc']

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
