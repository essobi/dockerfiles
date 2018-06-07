FROM tifayuki/java:7  
MAINTAINER team@lastbackend.com  
  
RUN apt-get update && \  
apt-get install -y wget unzip pwgen expect && \  
wget download.java.net/glassfish/4.0/release/glassfish-4.0.zip && \  
unzip glassfish-4.0.zip -d /opt && \  
rm glassfish-4.0.zip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENV PATH /opt/glassfish4/bin:$PATH  
  
ADD init.sh /init.sh  
ADD password_func.sh /password_func.sh  
ADD secure.sh /secure.sh  
RUN chmod +x /*.sh  
  
# 4848 (administration)  
EXPOSE 4848  
# 8080 (HTTP listener)  
EXPOSE 8080  
# 8181 (HTTPS listener)  
EXPOSE 8181  
CMD ["/init.sh"]

