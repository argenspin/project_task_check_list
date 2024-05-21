from odoo import models,api,fields

class TaskCheckList(models.Model):
    _name = "project.task.check.list"
    name = fields.Char(string="Name")
    project_task_id = fields.Many2one('project.task', string="Task Name")
    task_file = fields.Binary(string="Attach Checklist Document")
