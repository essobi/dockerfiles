FROM ubuntu:14.04  
MAINTAINER cfoguet  
  
RUN apt-get -y update && apt-get -y install git python-dev libglpk-dev python-
pip  
RUN apt-get install -y libxml2-dev libxslt1-dev python-tk  
RUN pip install --upgrade pip  
RUN pip install -e
git+https://github.com/cfoguet/iso2flux.git@phnm#egg=iso2flux  
  
ENTRYPOINT ["run_iso2flux.py"]  

