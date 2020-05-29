# Workshop 1 - Part 3 - Step 1
# $ python app.py --film-name=flubber --stars=3
# Should write "flubber, 3" to a file
# The app should support submitting multiple reviews (by repeatedly running python app.py)

import click

with open('filmreviews.csv', 'a') as f:
    @click.command()
    @click.option('--film_name', '-f', required=True, help='Enter name of film')
    @click.option("--stars", '-s', required=True, help='Enter film star rating', type=int)

    def main(film_name,stars):
        """Simple film review program that outputs to a file"""
        click.echo('{},{}'.format(film_name,stars))
        f.write('{},{}'.format(film_name,stars))
        f.write("\n")

    if __name__ == '__main__':
        main()