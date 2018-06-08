# Minecraftly Proxy Dockerfile  
FROM java:8u111  
  
RUN apt-get update -y  
RUN apt-get upgrade -y  
  
COPY src /data  
  
COPY run.sh /data  
  
#RUN exec chown minecraftly /data -R | sh  
VOLUME /data  
WORKDIR /data  
  
EXPOSE 25565  
#USER minecraftly  
#Start Minecraftly proxy. Add exec after CMD if need to run in PID 1  
CMD exec sed -i "s/server-id:.*/server-id: proxy-$(cat
/proc/sys/kernel/random/uuid)/" /data/plugins/RedisBungee/config.yml | sh &&
exec sh run.sh

