FROM birdhouse/slurm  
  
MAINTAINER Birdhouse <wps@dkrz.de>  
LABEL Description="Slurm with Emu WPS" Vendor="Birdhouse" Version="0.7.0"  
# install emu wps  
RUN conda install -y -c birdhouse -c conda-forge emu pywps=4 dill psycopg2
gunicorn=19.7  

