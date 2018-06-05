FROM java:7-jre  
  
ADD
https://repository.apache.org/content/repositories/releases/org/apache/activemq/apache-
activemq/5.14.1/apache-activemq-5.14.1-bin.tar.gz /tmp/  
ADD http://www.apache.org/dist/activemq/KEYS /tmp/  
ADD https://www.apache.org/dist/activemq/5.14.1/apache-
activemq-5.14.1-bin.tar.gz.asc /tmp/  
  
RUN cd /tmp/ && gpg --import KEYS && gpg --verify apache-
activemq-5.14.1-bin.tar.gz.asc  
  
RUN tar xvzf /tmp/apache-activemq-5.14.1-bin.tar.gz -C /opt/  
RUN chmod 755 /opt/apache-activemq-5.14.1  
RUN rm /tmp/KEYS && rm /tmp/*.gz  
  
EXPOSE 61616  
EXPOSE 61613  
EXPOSE 61614  
EXPOSE 8161  
ENTRYPOINT /opt/apache-activemq-5.14.1/bin/activemq console  

