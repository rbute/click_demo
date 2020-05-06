import click
from pkg_resources import iter_entry_points

EP_NAME = 'click_demo_plugins'


class MyCLI(click.Group):

    def list_commands(self, ctx):
        rv = {a.name: a.load() for a in list(iter_entry_points(EP_NAME))}
        return sorted(list(rv.keys()))

    def get_command(self, ctx, name):
        ep: list = list(iter_entry_points(EP_NAME, name=name))[0]
        ep = None if not ep else ep.load()
        return ep


@click.command(cls=MyCLI)
def cli():
    pass


if __name__ == '__main__':
    cli()
