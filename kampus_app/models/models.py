from odoo import fields, models

class mahasiswa (models.Model):
    _name = "mahasiswa"
    _description = "mahasiswa"

    name = fields.Char(string = "nama")
    code = fields.Char(string= "Nomor")
    tgl_masuk =  fields.Date(string="Tanggal Masuk")
    image= fields.Binary()
    state = fields.Selection([
        ('waiting', 'Witing'),
        ('success','Success'),
        ('fail','Fail'),
    ],default = 'waiting', string='Status')

    def button_success(self):
        self.state = 'success'
    def buttin_fail(self):
        self.state='fail'
