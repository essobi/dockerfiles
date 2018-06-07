#  
# Hansoft server Dockerfile  
#  
# https://github.com/patrikha/hansoftserver  
#  
# pull base image  
FROM progrium/busybox  
  
# install Hansoft server  
RUN \  
opkg-install curl unzip libuuid && \  
cd /tmp && \  
curl -k -o HansoftServerX64.zip -A "Mozilla/5.0 (compatible; MSIE 7.01;
Windows NT 5.0)" -L http://hansoft.com/downloads/latest-linux-server/ && \  
unzip -d /tmp/ HansoftServerX64.zip && \  
rm HansoftServerX64.zip  
COPY server.config /HansoftServer/  
COPY Backup /HansoftServer/  
COPY run.sh /HansoftServer/  
  
# define working directory  
VOLUME /HansoftServer  
  
# define default run command  
CMD ./run.sh  
  
# expose Hansoft server port  
EXPOSE 50256  

