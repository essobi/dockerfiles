FROM continuumio/miniconda3  
  
# Set the ENTRYPOINT to use /bin/bash (bash shell). Docker by default uses
/bin/sh.  
ENTRYPOINT ["/bin/bash", "-c"]  
SHELL ["/bin/bash", "-c"]  
  
# Conda supports delegating to pip to install dependencies  
# that aren’t available in anaconda or need to be compiled  
# for other reasons.  
RUN apt-get update --fix-missing  
RUN apt-get install -y \  
apt-utils \  
libpq-dev \  
build-essential \  
zip unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install --upgrade wheel  
  
# update conda  
RUN conda update --yes conda  
  
# Use the environment.yml to create the conda environment.  
COPY environment.yml /tmp/environment.yml  
RUN conda env create --file /tmp/environment.yml  
  
# Install PostgreSQL client  
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" >
/etc/apt/sources.list.d/pgdg.list  
RUN apt-get update && apt-get install -y python-software-properties software-
properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3  

