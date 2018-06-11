FROM ubuntu:trusty  
MAINTAINER troyswanson <gerphimum@gmail.com>  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install \  
build-essential \  
nginx \  
python \  
ruby \  
ruby-dev \  
nodejs  
  
RUN gem install jekyll --no-ri --no-rdoc  
  
ADD nginx.conf /etc/nginx/nginx.conf  
  
CMD ["nginx"]  
  
EXPOSE 80  

