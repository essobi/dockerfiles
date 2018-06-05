FROM ubuntu:latest  
  
ENV DEBIAN_FRONTEND='noninteractive' \  
JAVA_HOME='/usr/lib/jvm/java-8-openjdk-amd64' \  
BASEDIR='/usr/lib/unifi' \  
DATADIR='/usr/lib/unifi/data' \  
LOGDIR='/usr/lib/unifi/logs' \  
RUNDIR='/usr/lib/unifi/run' \  
JVM_MAX_HEAP_SIZE='1024M' \  
JVM_INIT_HEAP_SIZE='1024M' \  
MAINCLASS='com.ubnt.ace.Launcher' \  
MONGO_USE_INTERNAL_DB='false' \  
MONGO_DB_NAME='unifi'  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
gnupg2 \  
ca-certificates  
  
RUN echo 'deb https://www.ubnt.com/downloads/unifi/debian stable ubiquiti' >
/etc/apt/sources.list.d/unifi.list \  
&& apt-key adv --keyserver keyserver.ubuntu.com --recv 06E85760C0A52C50 \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
execstack \  
openjdk-8-jdk-headless \  
unifi \  
&& apt-get clean \  
&& rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*  
  
RUN mkdir -p "${RUNDIR}" "${LOGDIR}" "${DATADIR}"  
  
COPY config/docker-entrypoint /  
RUN chmod +x /docker-entrypoint  
  
WORKDIR /usr/lib/unifi  
EXPOSE 6789 8080 8443 8880 8843 3478/udp 10001/udp  
  
ENTRYPOINT [ "/docker-entrypoint" ]  
CMD [ "start" ]  

