FROM debian:jessie  
  
MAINTAINER Natanael Arndt <arndt@informatik.uni-leipzig.de>  
  
# Let the container know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# update package index  
# and install some basic required packages  
RUN apt-get update && \  
apt-get install -y git make curl php5-cli php5-curl && \  
rm -rf /var/lib/apt/lists/*  
  
# Prepare installations directory  
RUN rm -rf /var/www/* && mkdir -p /var/www/html/  
  
RUN curl https://getcomposer.org/composer.phar -o composer.phar && \  
chmod +x composer.phar && \  
mv composer.phar /usr/bin/composer  
RUN composer create-project --keep-vcs aksw/ontowiki /var/www/html/ dev-
develop  
  
WORKDIR /var/www/html/  
  
# this is only required for RDFauthor at the moment  
RUN git submodule init && \  
git submodule update  
  
RUN cp config.ini.dist config.ini  
  
# Add startscript and start  
ADD start.sh /start.sh  
ADD ow-docker.fig /ow-docker.fig  
  
VOLUME /var/www/html/  
  
CMD ["/bin/bash", "/start.sh"]  

