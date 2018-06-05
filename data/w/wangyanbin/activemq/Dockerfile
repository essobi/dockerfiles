#FROM webcenter/openjdk-jre:8  
FROM openjdk:7-jre  
#MAINTAINER Sebastien LANGOUREAUX <linuxworkgroup@hotmail.com>  
MAINTAINER wangyanbin@dayang.com.cn  
  
  
# Update distro and install some packages  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install vim curl -y && \  
apt-get install supervisor -y && \  
apt-get install logrotate -y && \  
apt-get install locales -y && \  
update-locale LANG=C.UTF-8 LC_MESSAGES=POSIX && \  
locale-gen en_US.UTF-8 && \  
dpkg-reconfigure locales && \  
rm -rf /var/lib/apt/lists/*  
  
# Lauch app install  
COPY assets/setup/ /app/setup/  
RUN chmod +x /app/setup/install &&\  
/app/setup/install  
  
# Copy the app setting  
COPY assets/init.py assets/run.sh /app/  
  
RUN chmod +x /app/*  
  
# Expose all port  
EXPOSE 8161  
EXPOSE 61616  
EXPOSE 5672  
EXPOSE 61613  
EXPOSE 1883  
EXPOSE 61614  
# Expose some folders  
VOLUME ["/data/activemq"]  
VOLUME ["/var/log/activemq"]  
VOLUME ["/opt/activemq/conf"]  
  
ENV ACTIVEMQ_CONF=/opt/activemq/conf.tmp ACTIVEMQ_DATA=/opt/activemq/data  
WORKDIR /opt/activemq  
  
#ENTRYPOINT ["/app/init"]  
CMD ["/app/run.sh"]  

