FROM nginx  
  
RUN rm -rf /etc/nginx/conf.d/*  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y curl  
  
RUN curl
https://github.com/kelseyhightower/confd/releases/download/v0.7.1/confd-0.7.1-linux-
amd64 -#Lo confd  
RUN mv confd /usr/local/bin/confd  
RUN chmod +x /usr/local/bin/confd  
  
RUN mkdir -p /etc/confd/{conf.d,templates}  
ADD ./nginx.conf.tmpl /etc/confd/templates/nginx.conf.tmpl  
ADD ./nginx.toml /etc/confd/conf.d/nginx.toml  
ADD ./run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/run.sh"]  

