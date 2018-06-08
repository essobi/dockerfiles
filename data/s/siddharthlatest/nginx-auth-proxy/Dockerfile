FROM nginx  
MAINTAINER Siddharth Kothari <siddharth@appbase.io>  
  
RUN apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install apache2-utils curl dnsutils vim  
  
COPY generate.sh /home/  
COPY default.conf /etc/nginx/conf.d/  
COPY esclusterinternal.key /etc/nginx/conf.d/  
COPY esclusterinternal.crt /etc/nginx/conf.d/  
COPY dhparams.key /etc/nginx/conf.d/  
  
WORKDIR /home  
  
RUN chmod +x generate.sh  
  
EXPOSE 80  
ENTRYPOINT ["/bin/bash","/home/generate.sh"]  

