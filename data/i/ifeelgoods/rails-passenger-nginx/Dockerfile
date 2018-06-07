FROM ubuntu:16.04  
MAINTAINER Matthieu Paret <matthieu@ifeelgoods.com>  
  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install git imagemagick build-essential libmysqlclient-dev mysql-
client libxslt-dev libxml2-dev curl python-software-properties software-
properties-common nano apt-transport-https ca-certificates tzdata -y  
  
RUN add-apt-repository ppa:brightbox/ruby-ng && apt-get update && apt-get
install ruby2.3 ruby2.3-dev -y  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 561F9B9CAC40B2F7
\  
&& echo 'deb https://oss-binaries.phusionpassenger.com/apt/passenger xenial
main' > /etc/apt/sources.list.d/passenger.list \  
&& apt-get update \  
&& apt-get install nginx-extras passenger -y  
  
COPY ./nginx/* /etc/nginx/  
RUN rm -rf /etc/nginx/sites-available/*  
COPY ./nginx/sites-available/* /etc/nginx/sites-enabled/  
COPY ./nginx/nginx_wrapper /usr/bin/nginx_wrapper  
RUN chmod +x /usr/bin/nginx_wrapper  
  
RUN ln -sf /dev/stdout /var/log/nginx/access.log  
RUN ln -sf /dev/stderr /var/log/nginx/error.log  
  
RUN mkdir -p /home/app  
ENV HOME /home/app  
RUN mkdir -p /home/app/source  
WORKDIR /home/app/source  
  
RUN echo 'gem: --no-rdoc --no-ri' >> ~/.gemrc  
RUN gem install bundler -v 1.14.6  
  
CMD export PATH=$PATH:$ADDITIONAL_PATH; /bin/echo -e "ADDITIONAL_PATH is
$ADDITIONAL_PATH\nPATH is $PATH"  
  
ONBUILD COPY . /home/app/source  
  
ONBUILD RUN chown -R nobody:www-data /home/app  

