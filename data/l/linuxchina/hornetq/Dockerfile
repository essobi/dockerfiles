FROM java:7u75  
  
MAINTAINER linux_china linux_china@hotmail.com  
  
ENV HORNETQ_VERSION 2.4.7  
ENV HORNETQ_HOME /opt/hornetq-${HORNETQ_VERSION}  
  
RUN \  
curl -O
http://get.jenv.mvnsearch.org/download/hornetq/hornetq-${HORNETQ_VERSION}.zip
&& \  
unzip -d /opt/ hornetq-${HORNETQ_VERSION}.zip && \  
rm hornetq-${HORNETQ_VERSION}.zip  
  
WORKDIR $HORNETQ_HOME/bin  
  
EXPOSE 5445 5455  
CMD ["./run.sh"]  

