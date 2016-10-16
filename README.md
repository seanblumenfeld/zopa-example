#zopa-example

##Requirements
Docker and Docker Compose are required to run this application. Installation guides can be found here:
* https://docs.docker.com/engine/installation/
* https://docs.docker.com/compose/install/

##Usage
This application uses make as its interface.
* To run the application do `make start`
* To run all tests do `make tests`
* To tear down the application do `make clean`
* To run the linter do `make lint`
* To run run and use the program do:
    * `make run`
    * `./app.py [market_file] [loan_amount]`
**Note: Please make sure to put copy your market file to within the repository in order for the application to be able to find it. Ideally it should be placed in the data directory of the project**
