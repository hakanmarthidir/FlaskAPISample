from flask import Flask, render_template

app = Flask(__name__)


@app.route('/mytemplate')
def template_index():
    return render_template('index.html')


@app.route('/mytemplate/<name>')
def template_name(name):
    return render_template('name.html', name=name)


@app.route('/mytemplate/teams')
def template_teams():
    teams = ('gs', 'fb', 'bjk')
    return render_template('teams.html', teamnames=teams)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
