#!/usr/bin/python
# -*- coding: utf-8 -*-

# Hive Colony Framework
# Copyright (c) 2008-2012 Hive Solutions Lda.
#
# This file is part of Hive Colony Framework.
#
# Hive Colony Framework is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Hive Colony Framework is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Hive Colony Framework. If not, see <http://www.gnu.org/licenses/>.

__author__ = "João Magalhães <joamag@hive.pt>"
""" The author(s) of the module """

__version__ = "1.0.0"
""" The version of the module """

__revision__ = "$LastChangedRevision$"
""" The revision number of the module """

__date__ = "$LastChangedDate$"
""" The last change date of the module """

__copyright__ = "Copyright (c) 2008-2012 Hive Solutions Lda."
""" The copyright for the module """

__license__ = "GNU General Public License (GPL), Version 3"
""" The license for the module """

global manager
global plugins

manager.ensure(plugins.api_medium)

API_PARAMETERS = {}
""" The parameters to be used to configure
the api client, should respect the default
configuration of the colony instance """

BASE_URL = "http://localhost:8080/dynamic/rest/mvc/medium/"
""" The base url to the target endpoint of
communication for the medium service """

# creates the client with the default parameters and then
# generates the structure with the defined base url and
# runs the remote call to update the message value
client = plugins.api_medium.create_client(API_PARAMETERS)
client.generate_medium_structure(BASE_URL)
client.set_message("Hello World", "information")
