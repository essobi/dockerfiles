FROM ubuntu:trusty  
MAINTAINER Philipp Eschenbach <philipp@uberall.com>  
  
RUN apt-get update && apt-get upgrade -y && apt-get install -y language-pack-
en tomcat7 && apt-get autoremove -y && apt-get clean all && service tomcat7
stop && rm -R /var/lib/tomcat7/webapps/*  
  
ENV LC_ALL en_US.UTF-8  
ENV LANGUAGE en_GB.UTF-8  
ENV LANG en_GB.UTF-8  
  
RUN sed -i 's/-Xmx128m -XX:+UseConcMarkSweepGC/-Xmx2048M -Xms768M
-XX:MaxPermSize=512m -XX:PermSize=256m -XX:+UseParallelGC/g'
/etc/default/tomcat7  
  
EXPOSE 8080  
  
ADD run.sh /root/run.sh  
RUN chmod +x /root/run.sh  
RUN mkdir /var/lib/tomcat7/data  
RUN chown tomcat7 /var/lib/tomcat7/data  
CMD ["/root/run.sh"]

