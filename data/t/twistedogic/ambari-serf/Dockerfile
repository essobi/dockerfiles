FROM twistedogic/ambari-base  
MAINTAINER Jordan Li  
  
ENV SERF_HOME /root/serf  
RUN mkdir $SERF_HOME && mkdir $SERF_HOME/bin && mkdir $SERF_HOME/etc  
  
RUN yum update -y && yum install -y unzip curl && yum clean all  
  
RUN wget https://dl.bintray.com/mitchellh/serf/0.6.4_linux_amd64.zip -P /tmp  
RUN unzip /tmp/0.6.4_linux_amd64.zip -d $SERF_HOME/bin && rm -f
/tmp/0.6.4_linux_amd64.zip  
  
COPY serf_init.sh $SERF_HOME/bin/serf_init.sh  
COPY updatehosts.json $SERF_HOME/etc/updatehosts.json  
COPY updatehosts.sh $SERF_HOME/bin/updatehosts.sh  
RUN chmod +x $SERF_HOME/bin/*  
  
COPY supervisord.conf /etc/supervisord.conf  
  
EXPOSE 22  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  
  

