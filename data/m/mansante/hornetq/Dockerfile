FROM java:8-jdk  
MAINTAINER mansante <mansante@gmail.com>  
  
ENV HORNETQ_VERSION 2.4.0.Final  
ENV HORNETQ_HOME /opt/hornetq-${HORNETQ_VERSION}  
  
RUN mkdir ${HORNETQ_HOME} \  
&& curl -sSL
http://downloads.jboss.org/hornetq/hornetq-${HORNETQ_VERSION}-bin.tar.gz \  
| tar -zxC ${HORNETQ_HOME} \--strip-components=1 \  
&& rm -f hornetq-${HORNETQ_VERSION}-bin.tar.gz  
  
ADD run.sh $HORNETQ_HOME/bin/  
  
WORKDIR $HORNETQ_HOME/bin  
  
EXPOSE 5445 5455  
CMD ["./run.sh"]  
  

