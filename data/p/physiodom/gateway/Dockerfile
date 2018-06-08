FROM mhart/alpine-node:0.10.48  
MAINTAINER Fabrice Le Coz <fabrice.lecoz@telecomsante.com>  
  
RUN apk add -U nginx supervisor && \  
npm install -g npm@3.10.5 && \  
mkdir -p /logs && \  
mkdir -p /config  
  
COPY nginx.conf /etc/nginx/  
COPY nginx.tmpl /etc/confd/templates/  
COPY supervisord.ini /etc/supervisor.d/  
  
# conf-watch install  
COPY conf-watch/ /opt/conf-watch/  
RUN cd /opt/conf-watch && \  
npm install && \  
chmod a+x /opt/conf-watch/confd-watch  
  
VOLUME ["/logs"]  
  
LABEL version="1.0"  
LABEL name="physiodom-GW"  
LABEL description="A nginx reverse proxy gateway"  
  
# Expose ports.  
EXPOSE 80  
# Define default command.  
CMD ["/usr/bin/supervisord"]  

