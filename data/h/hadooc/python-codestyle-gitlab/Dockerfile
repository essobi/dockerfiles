FROM ubuntu:16.04  
MAINTAINER Borni DHIFI <dhifi.borni@gmail.com>  
  
RUN apt-get update \  
&& apt-get install git python3-pip pylint -y  
  
RUN pip3 install pycodestyle pydocstyle flake8 hacking  
  
RUN pip3 install --upgrade git+https://github.com/oca/pylint-odoo.git  

