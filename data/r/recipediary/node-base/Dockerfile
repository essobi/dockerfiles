FROM ubuntu-debootstrap:14.04  
ENV DEBIAN_FRONTEND noninteractive  
ENV NODE_VERSION v0.11.16  
ENV NPM_VERSION 2.4.1  
ENV NODE_ENV production  
  
# Exclude npm cache from the image  
VOLUME ["/root/.npm"]  
  
# define mountable directories  
VOLUME ["/var/www"]  
  
ADD install.sh /  
RUN bash -xe /install.sh  
  
# define working directory.  
WORKDIR /var/www  
  

