FROM java:7  
MAINTAINER Sergei <serge@keeperlink.com>  
  
RUN apt-get update && \  
apt-get install -y wget unzip pwgen expect && \  
wget
http://download.oracle.com/glassfish/3.1.2.2/release/glassfish-3.1.2.2.zip &&
\  
unzip glassfish-3.1.2.2.zip -d /opt && \  
rm glassfish-3.1.2.2.zip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH /opt/glassfish3/bin:$PATH  
  
ADD *.sh /  
RUN chmod +x /*.sh  
  
# 4848 (administration), 8080 (HTTP listener), 8181 (HTTPS listener)  
EXPOSE 4848 8080 8181  
CMD ["/run.sh"]

