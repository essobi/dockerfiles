FROM java:8-jre  
  
  
# https://packages.graylog2.org/releases/graylog2-web-interface/graylog-web-
interface-1.3.4.tgz  
ENV GL_VERSION=1.3.4  
ENV GL_PACKAGE=graylog-web-interface-${GL_VERSION}.tgz  
ENV SOURCE_URL=https://packages.graylog2.org/releases/graylog2-web-
interface/${GL_PACKAGE}  
  
RUN \  
cd /tmp && \  
wget $SOURCE_URL -O $GL_PACKAGE && \  
tar xvzf $GL_PACKAGE && \  
rm -f $GL_PACKAGE && \  
mv /tmp/graylog-web-interface-${GL_VERSION} /graylog2  
  
COPY run_graylog2.sh /  
  
CMD ["/run_graylog2.sh"]  
  
EXPOSE 9000  

