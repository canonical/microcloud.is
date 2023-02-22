import flask

from canonicalwebteam import image_template
from canonicalwebteam.flask_base.app import FlaskBase
from canonicalwebteam.templatefinder import TemplateFinder

from webapp.views import get_user_country_by_ip

app = FlaskBase(
    __name__,
    "microcloud.is",
    template_folder="../templates",
    static_folder="../static",
    template_404="404.html",
)


@app.context_processor
def global_template_context():
    return {
        "path": flask.request.path,
    }


@app.context_processor
def utility_processor():
    return {"image": image_template}


template_finder_view = TemplateFinder.as_view("template_finder")

app.add_url_rule("/", view_func=template_finder_view)
app.add_url_rule("/<path:subpath>", view_func=template_finder_view)
app.add_url_rule("/user-country.json", view_func=get_user_country_by_ip)
