FROM python:2.7  
MAINTAINER Wangoru Kihara wangoru.kihara@badili.co.ke  
  
# Install build deps, then run `pip install`, then remove unneeded build deps
all in a single step. Correct the path to your production requirements file,
if needed.  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
mysql-client \  
libmysqlclient-dev \  
git \  
curl \  
wget \  
npm  
  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
  
# install bower  
RUN npm install --global bower  
  
# install uwsgi now because it takes a little while  
RUN pip install --upgrade pip && pip install uwsgi  
  
# Copy your application code to the container (make sure you create a
.dockerignore file if any large files or directories should be excluded)  
RUN mkdir /opt/azizi_amp/  
  
# Copy the requirements file and install the requirements  
COPY requirements.txt /opt/azizi_amp/  
RUN pip install -r /opt/azizi_amp/requirements.txt  
  
# add (the rest of) our code  
COPY . /opt/azizi_amp/  
  
# Change to the working dir, install bower and clone the vendor repo  
WORKDIR /opt/azizi_amp  
RUN bower install --allow-root  
RUN git clone \--depth=1 https://github.com/badili/odk_parser.git vendor  
  
# clone the odk_dashboard repo  
RUN git clone \--depth=1 https://github.com/badili/odk_dashboard.git
odk_dashboard  
  
ADD scripts /opt/scripts  
WORKDIR /opt/scripts  
  
RUN chmod a+x *.sh  
  
ENTRYPOINT ["/opt/scripts/entrypoint.sh"]

