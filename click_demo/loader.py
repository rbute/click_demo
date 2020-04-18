import click
from pkg_resources import iter_entry_points

EP_NAME = 'click_demo_plugins'


class MyCLI(click.Group):

    def list_commands(self, ctx):
        rv = {a.name: a.resolve() for a in list(iter_entry_points(EP_NAME))}
        return sorted(list(rv.keys()))

    def get_command(self, ctx, name):
        ep_list: list = [a for a in list(iter_entry_points(EP_NAME))]
        ep = None if not ep_list else ep_list[0].load()
        return ep


@click.command(cls=MyCLI)
def cli():
    pass


if __name__ == '__main__':
    cli()
