import click
from click_demo.loader import MyCLI


@click.command(cls=MyCLI)
@click.option('--name', default='Rakesh')
def click_demo_plugin_main(name):
    click.echo('Hello from click demo plugin {name}')


if __name__ == '__main__':
    click_demo_plugin_main()
