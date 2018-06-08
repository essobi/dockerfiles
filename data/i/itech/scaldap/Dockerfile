FROM debian:latest  
MAINTAINER itech  
  
  
RUN echo 'deb http://ftp.ca.debian.org/debian/ jessie-backports main contrib
non-free' >> /etc/apt/sources.list  
  
RUN apt-get update && \  
LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install --no-install-
recommends -y \  
openjdk-8-jre-headless ca-certificates-java && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN /var/lib/dpkg/info/ca-certificates-java.postinst configure  
  
COPY scaldap.jar /opt/  
  
EXPOSE 80  
ENV ADMIN_DN cn=admin,dc=example,dc=com  
ENV BASE_DN dc=example,dc=com  
  
  
CMD ["java","-jar","/opt/scaldap.jar","0.0.0.0","80"]  

