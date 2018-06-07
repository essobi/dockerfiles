FROM cedvan/ubuntu:14.04.20150206  
MAINTAINER dev@cedvan.com  
MAINTAINER maxime.sifflet@huttopia.com  
  
# Install apt-transport-https  
RUN apt-get -qq update \  
&& apt-get -qqy install apt-transport-https  
  
# Install pip  
RUN apt-get -qq update \  
&& apt-get -qqy install python-setuptools python-dev build-essential \  
&& easy_install pip \  
&& pip install --upgrade virtualenv  
  
# install fig  
RUN pip install -U docker-compose  
  
# Delete useless list packages  
RUN rm -rf /var/lib/apt/lists/*  
  
WORKDIR /src  
  
ENTRYPOINT ["docker-compose"]  

