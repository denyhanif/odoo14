from odoo import  models, fields , api

class Course(models.Model):
    _name = 'data.course' #namamodel
    _description =  "Ini rumasakit murah"

    name = fields.Char(
        string = "Title" ,
        reqired= True,
        help= "Fill course name"
    )

    description = fields.Text(
        # label
        string='Description'
    )

    active = fields.Boolean(
        string='Active',
        default = True
    )