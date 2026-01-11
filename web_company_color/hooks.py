# Copyright 2019 Alexandre Díaz <dev@redneboa.es>
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from .models.res_company import URL_BASE


def uninstall_hook(env):
    """Odoo 19+ hook - receives env directly."""
    env["ir.attachment"].search([("url", "=like", "%s%%" % URL_BASE)]).unlink()


def post_init_hook(env):
    """Odoo 19+ hook - receives env directly."""
    env["res.company"].search([]).scss_create_or_update_attachment()
