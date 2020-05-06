import click

# from click_demo.loader import cli
from click_demo.loader_failing import cli


@cli.command()
@click.option('--name', default='Dummy Value')
def main(name):
    click.echo(f'Hello from click demo plugin MPKG {name}')


if __name__ == '__main__':
    main()
