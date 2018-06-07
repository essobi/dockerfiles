FROM mhart/alpine-node:0.10.48  
MAINTAINER Fabrice Le Coz <fabrice.lecoz@telecomsante.com>  
  
RUN apk add -U nginx supervisor git && \  
npm install -g npm@3.10.5 && \  
npm install bower -g && \  
mkdir -p /src && \  
mkdir -p /logs && \  
mkdir -p /config  
  
COPY install/nginx.conf /etc/nginx/  
COPY install/physiodom.conf /etc/nginx/conf.d/  
  
# conf-register install  
COPY install/conf-register/* /opt/conf-register/  
RUN cd /opt/conf-register && \  
npm install && \  
chmod a+x /opt/conf-register/conf-register  
  
# conf-watch install  
COPY install/conf-watch/* /opt/conf-watch/  
RUN cd /opt/conf-watch && \  
npm install && \  
chmod a+x /opt/conf-watch/confd-watch  
  
COPY install/supervisord.ini /etc/supervisor.d/  
  
# Install the application  
COPY src /src  
RUN cd src && \  
npm install --production && \  
bower install  
  
VOLUME ["/config","/logs"]  
  
USER root  
  
LABEL version="1.1.20"  
LABEL name="physiodom-HHRPro"  
LABEL description="Physiodom HHRPro application"  
  
EXPOSE 80  
WORKDIR /src  
CMD ["/usr/bin/supervisord"]

