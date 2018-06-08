FROM python:3.6  
MAINTAINER Gaganpreet Arora <gaganpreet.arora@gmail.com>  
  
# Source: https://github.com/nikolaik/docker-python-
nodejs/blob/master/Dockerfile  
RUN apt-get update && apt-get install apt-transport-https  
  
RUN \  
echo "Installing Node and Yarn" && \  
echo "deb https://deb.nodesource.com/node_8.x jessie main" >
/etc/apt/sources.list.d/nodesource.list && \  
wget -qO- https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
\- && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" >
/etc/apt/sources.list.d/yarn.list && \  
wget -qO- https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add \- && \  
apt-get update && \  
apt-get install -yqq nodejs yarn && \  
rm -rf /var/lib/apt/lists/*  
  
RUN pip install --no-cache-dir pipenv  

