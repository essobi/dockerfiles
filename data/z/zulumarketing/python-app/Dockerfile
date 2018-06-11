# Python Web Application Container  
FROM zulumarketing/app-server:latest  
MAINTAINER Carlos Killpack <carlos@zulumarketing.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN locale-gen en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
  
RUN apt-get update > /dev/null \  
&& apt-get upgrade -y > /dev/null \  
&& apt-get clean > /dev/null \  
&& apt-get install -y python3 python-virtualenv python3-dev libpq-dev \  
postgresql-client libyaml-dev libjpeg-dev > /dev/null \  
&& apt-get clean > /dev/null \  

