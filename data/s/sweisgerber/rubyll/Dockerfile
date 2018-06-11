FROM ruby:2.4-stretch  
  
MAINTAINER Sebastian Weisgerber <weisgerber@cispa.saarland>  
  
# otherwise can see some encoding issues:  
# https://oncletom.io/2015/docker-encoding/  
ENV LANG=C.UTF-8  
RUN apt-get update  
RUN curl -sL http://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-key add
- &&\  
echo "deb http://deb.nodesource.com/node_8.x stretch main" >
/etc/apt/sources.list.d/nodesource.list &&\  
echo "deb-src http://deb.nodesource.com/node_8.x stretch main" >>
/etc/apt/sources.list.d/nodesource.list  
RUN apt-get update  
RUN apt-get install -y \  
build-essential \  
curl \  
ftp \  
libffi-dev \  
libpq-dev \  
ca-certificates \  
subversion \  
imagemagick \  
python3 \  
virtualenv \  
python-pip \  
python3-pip \  
nodejs \  
npm  
RUN rm -f /usr/bin/python && ln -s /usr/bin/python3.5 /usr/bin/python  
  
ENV RACK_ENV="production" \  
RAILS_ENV="production"  
CMD [ "irb" ]  

