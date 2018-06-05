# Graylog2-Server  
FROM java:7-jre  
  
RUN apt-get update && apt-get install -y pwgen  
  
# https://packages.graylog2.org/releases/graylog2-server/graylog-1.1.6.tgz  
ENV GL_VERSION=1.1.6  
ENV GL_PACKAGE=graylog-${GL_VERSION}.tgz  
ENV
SOURCE_URL=https://packages.graylog2.org/releases/graylog2-server/${GL_PACKAGE}  
  
RUN \  
cd /tmp && \  
wget $SOURCE_URL \  
&& tar xvzf $GL_PACKAGE \  
&& rm -f $GL_PACKAGE \  
&& mv /tmp/graylog-${GL_VERSION} /graylog2  
  
ADD config/graylog2.conf /etc/graylog2.conf  
  
ADD run_templates/run_graylog2.sh /graylog2/run_graylog2.sh  
  
CMD ["/graylog2/run_graylog2.sh"]  
  
EXPOSE 12900  
EXPOSE 12201  
EXPOSE 9300  

