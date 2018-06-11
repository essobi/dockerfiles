FROM phusion/baseimage:latest  
MAINTAINER Ximbesto  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update  
RUN apt-get install -y squid-deb-proxy-client  
RUN apt-get install -y default-jre  
RUN apt-get install -y unzip nmap  
#ADD OpenDJ-2.6.0.zip /  
ADD OpenDJ-2.7.0-20150307.zip /  
RUN useradd -d /var/lib/opendj -m -s /bin/bash opendj  
RUN chown opendj:opendj /OpenDJ-2.7.0-20150307.zip  
RUN su -s /bin/bash opendj -c "unzip /OpenDJ-2.7.0-20150307.zip -d /var/lib/"  
RUN rm -rf /OpenDJ-2.7.0-20150307.zip  
ADD opendj.properties /var/lib/opendj/opendj.properties  
ADD opendj.sh /tmp/  
ADD ximinitdj.sh /tmp/  
  
ADD assets/init /app/init  
RUN chmod 755 /app/init  
  
RUN chmod +x /tmp/ximinitdj.sh  
RUN chmod +x /tmp/opendj.sh  
  
VOLUME ["/tmp/xim"]  
RUN touch /tmp/xim/alaki  
  
EXPOSE 389 1686 1689 8080 4444  
#CMD ["/sbin/my_init"]  
ENTRYPOINT ["/app/init"]  
  
#CMD [app:start]  
#RUN mkdir /etc/service/opendj  
#RUN cd /var/lib/opendj;./setup --cli --propertiesFilePath opendj.properties
--acceptLicense --no-prompt  
#RUN /usr/sbin/enable_insecure_key  
#ADD opendj.sh /etc/service/opendj/run  
#RUN chmod +x /etc/service/opendj/run  
#VOLUME ["/var/lib/opendj/db"]  
#VOLUME ["/var/lib/opendj/log"]  

