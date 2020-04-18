import click
import pkg_resources

EP_NAME = 'click_demo_plugins'


class MyCLI(click.MultiCommand):

    def list_commands(self, ctx):
        rv = [a.name for a in list(pkg_resources.iter_entry_points(EP_NAME))]
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ep_list: list = [a for a in list(pkg_resources.iter_entry_points(EP_NAME)) if a.name == name]
        ep = None if not ep_list else ep_list[0].load()
        return ep


cli = MyCLI(
    name='demo_cli',
    help='This tool\'s sub-commands are loaded from entry points'
)

if __name__ == '__main__':
    cli()
