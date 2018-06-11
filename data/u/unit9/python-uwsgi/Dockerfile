FROM unit9/base:latest  
MAINTAINER Kamil Cholewiński <kamil.cholewinski@unit9.com>  
  
# Dependencies  
RUN apt-get update && \  
apt-get install --yes --no-install-recommends \  
python-all-dev \  
python-pip \  
python-wheel \  
uwsgi-plugin-python \  
&& rm -rf /var/cache/apt /var/lib/apt/lists  
  
# Create the space for the app  
RUN mkdir /app  
WORKDIR /app  
  
# Add "app" user to run uWSGI as  
RUN adduser --system --no-create-home --disabled-login --group app  

