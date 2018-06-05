# Graylog2-web  
FROM java:7-jre  
  
RUN apt-get update && apt-get install -y pwgen  
  
# https://packages.graylog2.org/releases/graylog2-web-interface/graylog-web-
interface-1.1.6.tgz  
ENV GL_VERSION=1.1.6  
ENV GL_PACKAGE=graylog-web-interface-${GL_VERSION}.tgz  
ENV SOURCE_URL=https://packages.graylog2.org/releases/graylog2-web-
interface/${GL_PACKAGE}  
  
RUN \  
cd /tmp && \  
wget $SOURCE_URL \  
&& tar xvzf $GL_PACKAGE \  
&& rm -f $GL_PACKAGE \  
&& mv /tmp/graylog-web-interface-${GL_VERSION} /graylog2-web  
  
ADD config/graylog-web-interface.conf /graylog2-web/conf/graylog-web-
interface.conf  
  
ADD run_templates/run_graylog2_web.sh /graylog2-web/run_graylog2_web.sh  
  
CMD ["/graylog2-web/run_graylog2_web.sh"]  
  
EXPOSE 9000  

