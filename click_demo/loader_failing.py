import click
from pkg_resources import get_entry_map

EP_NAME = 'click_demo_plugins'


def get_plugin_entrypoints(pkg):
    ep_map = get_entry_map(pkg).get(EP_NAME, {})
    ep_map = {k: v.load() for k, v in ep_map.items()}

    return ep_map


@click.group(commands=get_plugin_entrypoints('click_demo'))
def cli():
    pass


if __name__ == '__main__':
    cli()
