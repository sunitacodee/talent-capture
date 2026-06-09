import click
from flask.cli import with_appcontext
from app.utils.addressSeeder import AddressSeeder
from app.extensions import db
@click.command("address-seed")
@with_appcontext
def address_seeder():
    try:
        """Seeds the Nepal administrative location data (Provinces, Districts, Local Bodies, Wards)."""
        seeder = AddressSeeder(db.session)
        seeder.run_all_address_seededs()
        click.echo(click.style("Location seeding completed successfully!", fg="green"))
    except Exception as e:
        click.echo(click.style(f"❌ Seeding failed: {str(e)}", fg="red"), err=True)