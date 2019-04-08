# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ProjectTaskCustomizations(models.Model):
    _inherit = "project.task"

    subtask_effective_hours = fields.Float("Sub-tasks Hours Spent", compute='_compute_subtask_effective_hours', compute_sudo=True, store=True, help="Sum of actually spent hours on the subtask(s)", oldname='children_hours')