# FlexGet  
#  
# Version 3-ubuntu  
  
FROM ubuntu:16.04  
MAINTAINER Thomas Ingvarsson <ingvarsson.thomas@gmail.com>  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get update \  
&& apt-get install -y locales \  
&& locale-gen en_US.UTF-8 \  
&& apt-get install -y python3 python3-dev python3-pip unrar-free nodejs
nodejs-legacy \  
&& pip3 install --upgrade setuptools \  
&& pip3 install flexget \  
&& pip3 install transmissionrpc \  
&& pip3 install rarfile \  
&& pip3 install cfscrape \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["flexget", "daemon", "start"]

