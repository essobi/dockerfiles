# Debian: gruntjs  
#  
# VERSION 0.1  
# Pull the base image.  
FROM giordan/d-essentials  
  
MAINTAINER Gabriele Giuranno <gabrielegiuranno@gmail.com>  
  
# Set environment variables.  
ENV FILES conf/  
ENV TERM xterm-256color  
  
RUN apt-get update  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get update && apt-get install -y \  
nodejs \  
git \  
git-core \  
jq \  
bzip2  
RUN npm install -g grunt-cli bower  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD start.sh /usr/local/bin/start.sh  
# Configure executable to start php5-fpm.  
CMD ["start.sh"]  
  
# Expose ports.  
EXPOSE 9100  

