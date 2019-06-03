# coding: utf-8
#
# Copyright © Lyra Network.
# This file is part of Lyra plugin for Odoo. See COPYING.md for license details.
#
# Author:    Lyra Network (https://www.lyra.com)
# Copyright: Copyright © Lyra Network
# License:   http://www.gnu.org/licenses/agpl.html GNU Affero General Public License (AGPL v3)

from odoo import models, fields, api
from ..helpers import constants

class LyragwLanguage(models.Model):
    _name = 'lyragw.language'
    _description = 'Lyra language'
    _rec_name = 'label'
    _order = 'label'

    code = fields.Char()
    label = fields.Char(translate=True)

    @api.model_cr
    def init(self):
        languages = constants.LYRAGW_LANGUAGES

        for c, l in languages.items():
            lang = self.search([('code', '=', c)])

            if not lang:
                self.create({'code': c, 'label': l})
