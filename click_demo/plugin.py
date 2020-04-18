import click
from click_demo.loader import cli


@cli.command()
@click.option('--name', default='Rakesh')
def click_demo_plugin_main(name):
    click.echo(f'Hello from click demo plugin {name}')


if __name__ == '__main__':
    click_demo_plugin_main()
