FROM debian:jessie  
MAINTAINER Jean-Avit Promis "docker@katagena.com"  
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-radicale"  
LABEL version="0.9"  
  
ENV DEBIAN_FRONTEND=noninteractive \  
RADICALE_USER=user \  
RADICALE_PASSWORD=password  
  
RUN apt-get update --fix-missing && \  
apt-get update && \  
apt-get install -y -q radicale=0.9\\* apache2-utils  
  
RUN mkdir -p /var/log/radicale/  
  
COPY start.sh /start.sh  
RUN chmod +x /start.sh  
  
CMD /start.sh  
EXPOSE 5232  
VOLUME ["/var/lib/radicale/collections"]  

