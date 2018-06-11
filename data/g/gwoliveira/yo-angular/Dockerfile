FROM node:latest  
MAINTAINER Guilherme Willian de Oliveira <gwoliveira@gmail.com>  
  
# Add an yoangular user because grunt doesn't like being root  
RUN adduser --disabled-password --gecos "" yoangular  
  
# install yeoman  
RUN npm install -g grunt-cli bower yo generator-karma generator-angular  
  
# install sass compass  
RUN apt-get update && apt-get install -y ruby-full && \  
gem install sass compass  
  
# set HOME so 'npm install' and 'bower install' don't write to /  
ENV HOME /home/yoangular  
  
RUN mkdir /src && chown yoangular:yoangular /src  
WORKDIR /src  
  
# expose the working directory  
VOLUME ["/src"]  
  
USER yoangular  
EXPOSE 9000 35729  
CMD /bin/bash  

