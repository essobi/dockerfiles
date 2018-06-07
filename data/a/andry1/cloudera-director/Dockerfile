## Reference:  
## [1] https://github.com/sameersbn/docker-gitlab  
FROM centos:centos6  
MAINTAINER Antonin Bruneau <antonin.bruneau@gmail.com>  
  
COPY app/ /app/  
RUN /app/setup/install  
  
# All we're doing here is replacing the init script with one that starts
director-server into the  
# foreground and logs to stdout  
COPY cloudera-director-server.init /etc/init.d/cloudera-director-server  
COPY logback.xml /etc/cloudera-director-server/logback.xml  
COPY logback-access.xml /etc/cloudera-director-server/logback-access.xml  
  
EXPOSE 7189  
VOLUME /var/lib/cloudera-director-server  
  
ENTRYPOINT ["/etc/init.d/cloudera-director-server", "start"]  

