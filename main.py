#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import logging

from google.appengine.ext import webapp
from persistence import PersistenceHelper
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template


class MainHandler(webapp.RequestHandler):
    def get(self):
		helper = PersistenceHelper()
		topDiputados  = helper.getTopDiputadosIniciativas( 10 )
		downDiputados = helper.getDownDiputadosIniciativas( 10 )
		logging.info("funciona")
		for d in downDiputados:
			if d.numero_iniciativas == None:
				d.numero_iniciativas = 0
		template_values = { "topDiputados" :topDiputados, 
							"downDiputados":downDiputados }
		path = os.path.join(os.path.dirname(__file__), 'index.html')
		self.response.out.write(template.render(path, template_values))
		

def main():
	logging.getLogger().setLevel(logging.DEBUG)
	application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
	util.run_wsgi_app(application)


if __name__ == '__main__':
    main()