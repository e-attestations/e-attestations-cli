import click

@click.group()
@click.option('-v', '--verbose', count=True, default=False)
@click.pass_context
def cli(ctx, verbose):
    ctx.ensure_object(dict)
    ctx.obj['VERBOSE'] = verbose
    pass

@cli.command()
@click.option(  '--fragment', 
                default='12+Rue+du+chemin+des+femmes+91300+MASSY', 
                help='The address fragment to search',
                prompt=True)
@click.pass_context
def search(ctx, fragment):
    '''This script send a request to Open API Address an format the responses'''
    verbose=ctx.obj['VERBOSE']
    if(verbose):
        click.echo('Looking for address %s' % fragment)
    else:
        click.echo('Searching... %s' % fragment)

if __name__ == '__main__':
    cli(obj={})
