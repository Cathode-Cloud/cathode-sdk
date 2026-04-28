from __future__ import annotations

import click


@click.group()
@click.version_option(package_name="cathode")
@click.option(
    "--api-key", envvar="CATHODE_API_KEY", default=None, help="API key."
)
@click.pass_context
def main(ctx: click.Context, api_key: str | None) -> None:
    """Cathode Cloud CLI."""
    ctx.ensure_object(dict)
    ctx.obj["api_key"] = api_key


@main.command()
@click.pass_context
def whoami(ctx: click.Context) -> None:
    """Show the currently authenticated user."""
    from cathode.client import CathodeClient

    with CathodeClient(api_key=ctx.obj["api_key"]) as client:
        user = client.get("/v1/me")
        click.echo(f"Logged in as {user.get('email', 'unknown')}")
