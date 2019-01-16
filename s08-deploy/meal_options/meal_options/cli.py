import click

from . import app

@app.cli.group('my-group')
def my_group():
    """ my command group """
    pass


@my_group.command('my-command')
@click.option('--name', default='World')
def my_command(name):
    """ my great command """
    click.echo('Hello %s' % (name, ))

