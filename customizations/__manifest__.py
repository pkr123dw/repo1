# noinspection PyStatementEffect
#  -*- coding: utf-8 -*-
{
    'name' : 'Customizations',
    'version' : '1.0',
    'summary': 'Collection of customizations',
    'description': """
Description of manual adjustments
=================================
For the sub-task filter to work do:
-----------------------------------
insert in domain:
 | "'&',
 | ('parent_id', '!=', False),"
for record rules:
 - 'Project/Task: employees: follow required for follower-only projects'
 - 'Project/Task: portal users: (portal and following project) or (portal and following task)'
    """,
    'depends' : ['base', 'hr_timesheet'],
    'data': [
        'security/customizations_security.xml',
    ],
    'installable': True,
}