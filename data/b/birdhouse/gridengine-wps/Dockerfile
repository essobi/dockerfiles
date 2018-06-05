# vim:set ft=dockerfile:  
FROM birdhouse/gridengine  
MAINTAINER Birdhouse <wps@dkrz.de>  
  
LABEL Description="pywps gridengine demo" Vendor="Birdhouse" Version="0.1.0"  
# Install wps on worker  
RUN conda install -y -c birdhouse -c conda-forge emu pywps=4 dill psycopg2
gunicorn=19.7  
  
# add wps user  
RUN useradd -d /home/wps -m --uid 1000 wps  

