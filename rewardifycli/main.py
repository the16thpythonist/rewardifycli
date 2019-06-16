# third party
import click

from rewardify.env import EnvironmentConfig

# local
from rewardifycli.install import install
from rewardifycli.packs import packs
from rewardifycli.rewards import rewards
from rewardifycli.inventory import inventory
from rewardifycli.users import users
from rewardifycli.login import login
from rewardifycli.update import update


@click.group(name='rewardify')
def cli():
    environment_config: EnvironmentConfig = EnvironmentConfig.instance()
    environment_config.load()
    environment_config.init()


cli.add_command(install)
cli.add_command(packs)
cli.add_command(rewards)
cli.add_command(inventory)
cli.add_command(users)
cli.add_command(login)
cli.add_command(update)


if __name__ == '__main__':
    cli()
