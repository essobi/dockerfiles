FROM php:7.2-cli  
LABEL maintainer="Nazar Mokrynskyi <nazar@mokrynskyi.com>"  
  
COPY install-extensions.sh /  
RUN /install-extensions.sh && rm /install-extensions.sh  

