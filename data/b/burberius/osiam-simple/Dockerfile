# osiam-light  
FROM tomcat:8-jre8  
  
MAINTAINER Jens Oberender <j.oberender@tarent.de>  
  
#### update/install packages ####  
RUN echo 'force-unsafe-io' | tee /etc/dpkg/dpkg.cfg.d/02apt-speedup && \  
echo 'DPkg::Post-Invoke {"/bin/rm -f /var/cache/apt/archives/*.deb ||
true";};' | tee /etc/apt/apt.conf.d/no-cache && \  
DEBIAN_FRONTEND=noninteractive apt-get update -y && apt-get dist-upgrade -y &&
apt-get install mksh && \  
apt-get clean && rm -rf /var/cache/apt/*  
  
#### osiam ####  
RUN mkdir /etc/osiam  
  
COPY install.sh /install/  
RUN /install/install.sh  
  
ADD setenv.sh /usr/local/tomcat/bin/  
  
RUN sed -i
"/^shared\\.loader=/c\shared.loader=/var/lib/tomcat8/shared/classes,/var/lib/tomcat8/shared/*.jar,/etc/osiam"
/usr/local/tomcat/conf/catalina.properties  
  
# expose tomcat and pop3 ports  
EXPOSE 8080  
# start up  
CMD ["catalina.sh", "run"]  

