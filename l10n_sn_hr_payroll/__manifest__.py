# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (c) Optesis 2018 www.optesis.com___this is updating realease_c

{
    'name': 'Paie Sénégalaise',
    'version': '14.0.1',
    'author': 'Optesis ',
    'category': 'Localization',
    'description': """
Senegal Payroll Rules.
=====================
    - Configuration of hr_payroll for Senegal localization
                    """,
    'website': 'http://www.optesis.com',
    'depends': ['optipay', 'l10n_pcgo'],
    'data': [
        'security/ir.model.access.csv',
        'data/salary_rule_data.xml',
        'data/chart_data.xml',
        'data/salary_rule_foreign_data.xml',
        'views/payroll_chart_template_views.xml',
        'views/multi_company_view.xml',
    ],

}
