# Set the base image  
FROM debian  
  
# Dockerfile author / maintainer  
MAINTAINER Joseph Grainger <josephgrainger@gmail.com>  
  
# Update application repository list and install the Redis server.  
RUN apt-get update  
RUN apt-get -qq install curl  
RUN apt-get -qq install git  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -  
RUN apt-get install -y nodejs  
RUN curl -sL https://github.com/git-ftp/git-ftp/archive/1.3.3.tar.gz | tar xz  
RUN cp git-ftp-1.3.3/git-ftp /usr/bin/.  
RUN chmod +x /usr/bin/git-ftp  
RUN rm -r git-ftp-1.3.3  
RUN npm install -g yarn  
RUN npm install -g gulp  
RUN mkdir repo  
  
WORKDIR /repo  

