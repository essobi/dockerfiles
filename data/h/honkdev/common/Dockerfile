FROM honkdev/ubuntu-base:1.0.2  
MAINTAINER HONK Technologies, Inc.  
  
RUN apt-get -y update \  
&& apt-get -y install \  
liblzma-dev \  
libmagickwand-dev \  
libcurl4-openssl-dev \  
libpq-dev \  
postgresql-9.5=9.5.7* \  
nginx=1.10.3* \  
&& rm -rf /var/lib/apt/lists/*  
  
# NodeJS LTS v6  
RUN n 6.11.1  
  
# Python 2.7.13  
RUN pyenv install 2.7.13 && pyenv global 2.7.13  
  
# Ruby 2.3.4  
RUN rbenv install 2.3.4 && rbenv global 2.3.4  

