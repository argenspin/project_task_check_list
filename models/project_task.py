from odoo import models,fields,api

class ProjectTask(models.Model):
    _inherit = "project.task"

    checklist_task_file = fields.Binary(string="Add Document")
    task_checklist_ids = fields.Many2many('project.task.check.list',string="Checklist Tasks")
    checklist_documents_count = fields.Integer(compute="_compute_checklist_documents_count")
    checklist_progress = fields.Integer(compute="_compute_checklist_progress")

    def _compute_checklist_progress(self):
        for record in self:
            checklist_documents_count = self.env['project.task.check.list'].search_count([('project_task_id','=',record.id)])
            try:
                record.checklist_progress = int( len(record.task_checklist_ids) / checklist_documents_count * 100 )
            except ZeroDivisionError:
                record.checklist_progress = 0
    def _compute_checklist_documents_count(self):
        for record in self:
            record.checklist_documents_count = self.env['project.task.check.list'].search_count([('project_task_id','=',record.id)])

    def action_open_checklist_documents(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Checklist Documents',
            'res_model': 'project.task.check.list',
            'views':[[False,'tree'],[False,'form']],
            'target': 'current',
            'context': {'default_project_task_id':self.id},
            'domain': [('project_task_id','=',self.id)]
        }