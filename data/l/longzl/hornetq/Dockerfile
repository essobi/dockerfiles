FROM java:8-jdk  
  
ENV HORNETQ_VERSION 2.4.0.Final  
ENV HORNETQ_HOME /opt/hornetq-2.4.0.Final  
  
RUN mkdir /opt/hornetq-2.4.0.Final \  
&& curl -sSL http://downloads.jboss.org/hornetq/hornetq-2.4.0.Final-bin.tar.gz
\  
| tar -zxC /opt/hornetq-2.4.0.Final --strip-components=1 \  
&& rm -f hornetq-2.4.0.Final-bin.tar.gz  
  
RUN chmod a+x /opt/hornetq-2.4.0.Final/bin/run.sh  
  
EXPOSE 5445 5455  
CMD ["/opt/hornetq-2.4.0.Final/bin/run.sh"]  

