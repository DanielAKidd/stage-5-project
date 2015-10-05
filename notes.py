import os
import urllib

import webapp2
import jinja2


template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
								autoescape=True)


class Handler(webapp2.RequestHandler):
	"""Helper methods for dealing with templates"""
	def write(self, *a, **kw):
		self.response.out.write(*a, **kw)

	def render_str(self, template, **params):
		t = jinja_env.get_template(template)
		# a template object calling IT'S method render. This render method
		# accepts a dictionary of values to substitute
		return t.render(params) 

	def render(self, template, **kw):
		self.write(self.render_str(template, **kw))


class MainPage(Handler):
	"""Main handler"""
	def get(self):
		self.render("jsNotes.html")
		#self.response.out.write('Hello, webapp World!')

class apiPage(Handler):
	def get(self):
		self.render("apiNotes.html")
#temp handlers
class bigProb(Handler):
	def get(self):
		self.render("bigProblems.html")
class rp(Handler):
	def get(self):
		self.render("recursionParallelNotes.html")

app = webapp2.WSGIApplication([('/', MainPage),
							   ("/apiNotes", apiPage),
							   ("/bigProblems", bigProb),
							   ("/rp", rp)],
							  debug=True)