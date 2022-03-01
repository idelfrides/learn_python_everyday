#!/usr/bin/python
#enconding: utf-9

from webScraping.web_scraping import WebScraper
from abstract_classes import (
    Person, Dog,
    Cat, Lion
)


def run_main_app():

    print('\n\n THIS IS THE MAIN MODULE OF THIS APP \n\n')

    scrap_obj = WebScraper()

    # url = ''

    scrap_obj.scraping_weather()


    return



# product_analysis
# weather_analysis
# climate_analysis#
# descout_produt



def run_abstract_class():
    human = Person()
    human.move()

    dog = Dog()
    dog.move()

    cat = Cat()
    cat.move()

    lion = Lion()
    lion.move()




if __name__ == '__main__':
    # run_main_app()
    run_abstract_class()
