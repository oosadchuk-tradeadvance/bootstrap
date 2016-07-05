# -*- coding: utf-8 -*-
from openerp import http


class TestChart(http.Controller):
    @http.route('/my_chart', auth='public', website=True)
    def index(self, **kw):

        return http.request.render('website_trad.index', {})