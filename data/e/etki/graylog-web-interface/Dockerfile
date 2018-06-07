FROM java:8  
ENV GRAYLOG_SERVER_URI= \  
VERSION=1.3.4  
EXPOSE 80  
ADD https://packages.graylog2.org/releases/graylog2-web-interface/graylog-web-
interface-${VERSION}.tgz \  
/tmp/graylog-web-interface.tgz  
  
# you may use following instruction for direct archive copying instead of  
# downloading it every time  
#COPY graylog-web-interface-1.2.2.tgz /tmp/graylog-web-interface.tgz  
RUN tar -xzvf /tmp/graylog-web-interface.tgz -C /tmp  
RUN mv /tmp/graylog-web-interface-${VERSION} /usr/local/graylog && \  
rm /tmp/graylog-web-interface.tgz  
ADD bin/* /usr/local/graylog/bin/  
ADD configuration/graylog.conf.template
/usr/local/graylog/graylog.conf.template  
  
CMD ["/usr/local/graylog/bin/graylog-docker-wrapper.sh"]  

