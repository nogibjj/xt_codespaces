#!/usr/bin/env python


import click
from dblib.querydb import querydb
from dblib.querydb import find_most_least_year
from dblib.querydb import find_data_intro
from dblib.querydb import amount_increase

# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
@click.option(
    "--query",
    default="SELECT * FROM default.netflix_1_csv LIMIT 2",
    help="SQL query to execute",
)
def cli_query(query):
    """Execute a SQL query"""
    querydb(query)


@cli.command()
@click.option("--year", default=2022, help="Find move in Year 2022, Limit 5")
def query_year(year):
    """Given a year, find the country with the most population and least population"""
    find_most_least_year(year)


@cli.command()
# @click.option("--intro", help="introduce your dataset :)")
def data_intro():
    find_data_intro()


@click.command()
@click.option("--years", nargs=2, type=int)
def year_change(years):
    a, b = years
    click.echo(f"{a} / {b}")
    amount_increase(a, b)


# run the CLI
if __name__ == "__main__":
    cli.add_command(cli_query)
    cli.add_command(query_year)
    cli.add_command(data_intro)
    cli.add_command(year_change)
    cli()
