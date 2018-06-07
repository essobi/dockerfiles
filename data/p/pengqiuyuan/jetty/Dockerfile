FROM java:8-jdk  
  
MAINTAINER pengqiuyuanfj@gmail.com  
# cribbed from cjlyth/jetty  
WORKDIR /opt  
ENV VERSION 8.1.17.v20150415  
RUN echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure -f noninteractive
tzdata  
RUN curl "http://mirrors.ibiblio.org/eclipse/jetty/$VERSION/dist/jetty-
distribution-$VERSION.tar.gz" | tar xvfz -  
RUN mv jetty-distribution-$VERSION jetty  
ADD etc /opt/jetty/etc  
CMD /opt/jetty/bin/jetty.sh -d supervise  
  
EXPOSE 8080  

