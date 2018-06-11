FROM ubuntu:vivid  
  
MAINTAINER Ramon Brooker <rbrooker@aetherealmind.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# to allow supervisor to be installed  
RUN echo exit 101 > /usr/sbin/policy-rc.d  
RUN chmod +x /usr/sbin/policy-rc.d  
  
# for setting  
ENV LS_VERSION_MAJOR=1.5  
ENV LS_VERISON_MINOR=1.5.0-1  
# install need java run time and update system  
RUN apt-get update && apt-get -y upgrade &&apt-get install -y openjdk-7-jre-
headless logrotate  
  
# get and install logstash  
ADD
http://download.elastic.co/logstash/logstash/packages/debian/logstash_${LS_VERISON_MINOR}_all.deb
/  
  
RUN dpkg -i logstash_${LS_VERISON_MINOR}_all.deb  
  
# Clean up  
RUN apt-get clean  
RUN rm /logstash_${LS_VERISON_MINOR}_all.deb  
  
# Copy of run script  
COPY run.sh /  
RUN chmod +x /run.sh  
  
# add a time stamp  
COPY set-time.sh /  
RUN chmod +x /set-time.sh  
RUN /set-time.sh  
  
VOLUME ["/etc/logstash","/var/log/logstash"]  
  
# ElasticSeach  
EXPOSE 9200  
# Syslog  
EXPOSE 514  
# snmptrap  
EXPOSE 1062  
CMD ["./run.sh"]  
  

