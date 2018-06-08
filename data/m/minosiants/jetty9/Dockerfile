#  
#  
## VERSION 0.1.0  
FROM minosiants/java7  
MAINTAINER Kaspar Minosiants k@minosiants.com  
  
# Install Jetty9  
RUN \  
/usr/bin/wget \  
http://mirror.tspu.ru/eclipse/jetty/stable-9/dist/jetty-
distribution-9.2.1.v20140609.tar.gz \  
-O /tmp/jetty9.tar.gz && \  
mkdir /opt/jetty9 && \  
/bin/tar -xzf /tmp/jetty9.tar.gz -C /opt/jetty9 --strip-components=1 &&\  
rm /tmp/jetty9.tar.gz  
  
VOLUME /opt/jetty9  
  
EXPOSE 8080  
# run jetty  
CMD ["/opt/jetty9/bin/jetty.sh", "run"]

