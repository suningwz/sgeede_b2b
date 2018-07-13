# -*- encoding: utf-8 -*-
# Python source code encoding : https://www.python.org/dev/peps/pep-0263/
##############################################################################
#
#    OpenERP, Odoo Source Management Solution
#    Copyright (c) 2015 Antiun Ingeniería S.L. (http://www.antiun.com)
#                 Endika Iglesias <endikaig@antiun.com>
#                 Antonio Espinosa <antonioea@antiun.com>
#                 Daniel Góme-Zurita <danielgz@antiun.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "SGEEDE Infinite Scroll",
    "version": "1.0",
    "category": "Custom Development",
    "summary": """SGEEDE Infinite Scroll. Allow infinite scroll in Products without using pagination anymore.""",
    "description": """SGEEDE Infinite Scroll. Allow infinite scroll in Products without using pagination anymore.""",
    "author": "SGEEDE",
    "website": "http://www.sgeede.com",
    "depends": ['website', 'website_sale'],
    "init_xml": [],
    'update_xml': [
        'views/frontend.xml',
        'views/templates.xml'
    ],
    'qweb': ['static/src/xml/*.xml'],
    'demo_xml': [],
    'installable': True,
    'active': False,
    'price': 14.99,
    'currency': 'EUR',
    'images': [
        'images/main_screenshot.png',
        'images/sgeede.png'
    ]
}

