FROM node:7.4.0  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y mysql-client nano gzip wget \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir -p /usr/share/biterika/navigator-collector  
WORKDIR /usr/share/biterika/navigator-collector  
ENV appDir /usr/share/biterika/navigator-collector  
COPY ./ /usr/share/biterika/navigator-collector  
RUN cd /usr/share/biterika/navigator-collector && npm install  
  
RUN chmod +x /usr/share/biterika/navigator-collector/docker-entrypoint.sh  
RUN chmod +x /usr/share/biterika/navigator-collector/data/update.sh  
  
ENTRYPOINT ["/usr/share/biterika/navigator-collector/docker-entrypoint.sh"]  
  
EXPOSE 8889  

