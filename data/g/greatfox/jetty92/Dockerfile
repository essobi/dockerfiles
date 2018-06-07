FROM greatfox/oraclejdk8  
MAINTAINER Liang Dong <greatfox@gmail.com>  
  
RUN wget -qO /dev/stdout
http://download.eclipse.org/jetty/stable-9/dist/jetty-
distribution-9.2.7.v20150116.tar.gz | tar zxv -C /opt/  
RUN ln -s /opt/jetty* /opt/jetty  
RUN useradd jetty -U -s /bin/false  
RUN chown -R jetty:jetty /opt/jetty  
  
RUN echo 'JAVA_HOME=/usr/lib/jvm/java-8-oracle' >> /etc/default/jetty  
RUN echo 'JETTY_HOME=/opt/jetty' >> /etc/default/jetty  
RUN echo 'NO_START=0' >> /etc/default/jetty  
RUN echo 'JETTY_ARGS=jetty.port=8080' >> /etc/default/jetty  
RUN echo 'JETTY_HOST=0.0.0.0' >> /etc/default/jetty  
RUN echo 'JETTY_USER=jetty' >> /etc/default/jetty  
RUN echo '/opt/jetty/bin/jetty.sh start' >> /initrc  
  
EXPOSE 8080  

