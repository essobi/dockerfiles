FROM ubuntu:14.04  
MAINTAINER Jin Park <forjin@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y \  
npm \  
nodejs \  
build-essential \  
python3 \  
python3.4-dev \  
virtualenvwrapper \  
python3-pip \  
python3-psycopg2 \  
git \  
\--no-install-recommends && \  
which node || apt-get install -y nodejs-legacy && \  
npm install -g bower  
  
RUN pip3 install -vU setuptools  
  
# Install dependencies before copying full source directory. This speeds up  
# Docker rebuilds.  
COPY requirements.txt /tmp/  
WORKDIR /tmp  
RUN pip3 install -r requirements.txt  
  
COPY bower.json /tmp/  
RUN bower \  
\--allow-root \  
\--config.interactive=false \  
\--config.directory=bower_components \  
\--force-latest \  
install  
  
# Copy application to container. For development, mount a volume over this  
# directory.  
RUN mkdir -p /var/web/app  
COPY ./app /var/web/app  
RUN mkdir -p /var/web/template  
COPY ./template /var/web/template  
RUN mkdir -p /var/web/static  
  
WORKDIR /var/web/app  
RUN mv /tmp/bower_components /var/web/static/bower_components  
  
EXPOSE 80  
CMD ["python3", "app.py"]  

