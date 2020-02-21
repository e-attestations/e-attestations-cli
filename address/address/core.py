import click
from eabanner import colored
from colorama import init, Fore, Style
from .getAddress import getAddress

# Initialize colorama
init()

@click.group()
@click.option('-v', '--verbose', count=True, default=False)
@click.pass_context
def cli(ctx, verbose):
    '''CLI commands that search and fetch addresses'''
    ctx.ensure_object(dict)
    ctx.obj['VERBOSE'] = verbose
    if (verbose):
        colored()
    pass


@cli.command()
@click.argument('fragment', default='12+Rue+du+chemin+des+femmes+91300+MASSY')
@click.pass_context
def search(ctx, fragment):
    '''Send a request to Open API Address and format the responses
    The error is accessible through the verbose mode
    '''
    verbose = ctx.obj['VERBOSE']
    if (verbose):
        click.echo(Fore.BLUE + 'Looking for address %s' % fragment)
        click.echo(Style.RESET_ALL)

    # Call the API
    response = getAddress(fragment, verbose)
    click.echo(response)

if __name__ == '__main__':
    cli(obj={})
