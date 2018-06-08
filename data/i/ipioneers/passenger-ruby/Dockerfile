FROM phusion/passenger-ruby23  
  
MAINTAINER Ain Tohvri <at@interactive-pioneers.de>  
  
ENV HOME /root  
  
# Install Node.js and other dependencies  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get install -y \  
nodejs \  
libpcre3-dev \  
libcurl4-gnutls-dev \  
libgmp3-dev \  
mysql-client \  
postgresql-client \  
ruby2.3-dev \  
imagemagick \  
libmagickwand-dev \  
graphviz \  
wget  
  
RUN gem install bundler --no-ri --no-rdoc  
  
# Enable nginx  
RUN rm -f /etc/service/nginx/down /etc/nginx/sites-enabled/default  
  
# Cleanup  
RUN apt-get autoremove -y  
  
EXPOSE 80 443  
WORKDIR /home/app  
  
CMD ["/sbin/my_init"]  

