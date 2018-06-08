FROM python:2.7  
MAINTAINER Friedrich Lindenberg <friedrich@pudo.org>  
  
RUN pip install -q unicodecsv==0.14.1 normality>=0.4.2 fingerprints>=0.4.0 \  
countrynames jsonschema>=2.6.0 requests>=2.13 lxml xlrd six sqlalchemy>=1.1 \  
dalet boto3  
COPY . /libsanctions  
RUN cd /libsanctions && pip install -q -e .  

