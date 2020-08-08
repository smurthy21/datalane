import sys
import click
from datalane.workflow import Workflow

@click.group()
@click.pass_context
def cli(ctx):
    pass

@cli.command(context_settings = dict( ignore_unknown_options = True,
                                      allow_extra_args = True,
                                      help_option_names = ['-h', '?', '--help'],)
             )
@click.option('--yml', type=click.Path(exists=True))
@click.option('--rerun', is_flag = True)
@click.pass_context
def chug(ctx, rerun, yml):

    context_variables = dict()

    for item in ctx.args:
        context_variables.update([item.split('=')])

    workflow = Workflow(yml, rerun, context_variables)

    try:
        workflow.execute()
    except Exception as e:
        print(str(e))
        sys.exit(1)

    print('I am in done within run python file')
