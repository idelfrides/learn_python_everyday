#!/usr/bin/python
#enconding: utf-9


from webScraping.web_scraping import WebScraper
from abstract_classes import (
    Eagle, Person, Dog,
    Cat, Lion
)
from libs.lib_manager import (
    print_log
)

def run_main_app():

    print_log(f'THIS IS THE MAIN MODULE OF THIS APP \n\n')

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
    human.name_type = 'MR OBAMA'
    human.move()

    dog = Dog()
    dog.name_type = 'BOBY DOG'
    dog.move()

    cat = Cat()
    cat.name_type = 'NICKY CAT'
    cat.move()

    lion = Lion()
    lion.name_type = 'FINCH LION'
    lion.move()

    eagle = Eagle()
    eagle.name_type = 'FLY'
    eagle.move()



if __name__ == '__main__':
    # run_main_app()
    run_abstract_class()
