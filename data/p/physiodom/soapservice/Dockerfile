FROM mhart/alpine-node:0.10.48  
MAINTAINER Fabrice Le Coz <fabrice.lecoz@telecomsante.com>  
  
RUN apk add -U supervisor git && \  
npm install -g npm@3.10.5 && \  
mkdir -p /src && \  
mkdir -p /logs && \  
mkdir -p /config  
  
# conf-register install  
COPY install/conf-register/* /opt/conf-register/  
RUN cd /opt/conf-register && \  
npm install && \  
chmod a+x /opt/conf-register/conf-register  
  
COPY install/supervisord.ini /etc/supervisor.d/  
  
# Install the application  
COPY src /src  
RUN cd src && \  
npm install --production  
  
VOLUME ["/config","/logs"]  
  
USER root  
  
LABEL version="1.1.19-pre"  
LABEL name="physiodom-SOAPService"  
LABEL description="SOAP service"  
  
EXPOSE 80  
WORKDIR /src  
CMD ["/usr/bin/supervisord"]

