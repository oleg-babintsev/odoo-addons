# -*- coding: utf-8 -*-
##############################################################################
#
#    open2bizz
#    Copyright (C) 2020 open2bizz (open2bizz.nl).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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
    "name": "project_task_planning_o2b",
    'summary': 'Project Planning per week Open2Bizz',
    "description": 'Project Planning per week Open2Bizz',
    "version": "1.0",
    "author": "Open2bizz",
    "website": "http://www.open2bizz.tech",
    "license": "AGPL-3",
    "category": "Project",
    "installable": True,
    "depends": [
        "project",
    ],
    "data": [
             "data/project_tags.xml",
             "views/project_task.xml",
    ],
}

