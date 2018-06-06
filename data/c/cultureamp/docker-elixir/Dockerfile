FROM elixir:1.5  
MAINTAINER David Carlin <david.carlin@cultureamp.com>  
ENV REFRESHED_AT 2017-11-20  
RUN ["/bin/bash", "-c", "set -o pipefail && wget --quiet -O -
https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -"]  
  
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ trusty-pgdg main" > \  
/etc/apt/sources.list.d/pgdg.list  
  
RUN apt-get update  
RUN apt-get install -y \  
postgresql-client-9.5 \  
curl \  
wget \  
git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN wget
https://github.com/jwilder/dockerize/releases/download/v0.5.0/dockerize-linux-
amd64-v0.5.0.tar.gz  
RUN tar -C /usr/local/bin -xzvf dockerize-linux-amd64-v0.5.0.tar.gz  

