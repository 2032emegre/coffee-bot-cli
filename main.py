import click
from coffee_advisor import CoffeeAdvisor

@click.command()
@click.option('--mood', prompt='現在の気分を教えてください')
def main(mood):
    """気分に合わせてコーヒーを提案するCLIツール"""
    advisor = CoffeeAdvisor()
    recommendation = advisor.get_coffee_recommendation(mood)
    
    click.echo("\n=== コーヒー提案 ===")
    click.echo(recommendation["response"])

if __name__ == '__main__':
    main() 