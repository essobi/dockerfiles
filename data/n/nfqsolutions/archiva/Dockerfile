FROM nfqsolutions/centos:7  
MAINTAINER solutions@nfq.com  
  
# Instalacion previa  
RUN sudo yum install -y wget  
  
# Variables de entorno  
ENV JAVA_HOME=/solutions/app/java \  
JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8 \  
ARCHIVA_HOME=/solutions/app/archiva \  
JAVA_VERSION=8u92 \  
ARCHIVA_VERSION=2.2.0  
ENV PATH=$PATH:$JAVA_HOME/bin:$ARCHIVA_HOME/bin  
  
# Script de arranque  
COPY archiva.sh /solutions/  
RUN chmod 777 /solutions/archiva.sh && \  
chmod a+x /solutions/archiva.sh && \  
sed -i -e 's/\r$//' /solutions/archiva.sh  
  
# Volumenes para el docker  
VOLUME /solutions/app  
  
# Puerto de salida del docker  
EXPOSE 8080  
# Configuracion supervisor  
COPY supervisord.conf /etc/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]

