# Dockerfile to create a node.js container running rTail Server  
#  
# This Docker Container exposes a Web Server in the 8181 port and listen on
9191 port for UDP traffic.  
# UDP is stateless and is used instead of TCP because has better performance.  
# Both 8181 and 9191 ports are open without authentication. The recomendation
is to apply some filter rule in the Firewall.  
#  
# Usage:  
#  
# Previous steps:  
# 1) $ git clone https://github.com/chilcano/docker-rtail-server.git  
# 2) $ cd docker-rtail-server  
#  
# Build image:  
# $ docker build --rm -t chilcano/rtail-server .  
#  
# Run container:  
# $ docker run -d -t --name=rtail-srv -p 8181:8181 -p 9191:9191/udp
chilcano/rtail-server  
# $ docker run -d -t --name=rtail-srv-nc -p 8181:8181 -p 8182:8182 -p
9191:9191/udp -p 9192:9192/udp chilcano/rtail-server  
#  
# Check the rTail Server:  
# Just open a rTail Server Web Console from a browser with this URL
http://<IP_ADDRESS_RTAIL_CONTAINER>/8181  
# But if you want check if rTail Server Container is reacheable remotely (from
other VM), just execute this:  
#  
# // Use netcat instead of Telnet because Telnet doesn't use UDP  
# $ nc -vuzw 3 192.168.99.100 9191  
# Connection to 192.168.99.100 9191 port [udp/*] succeeded!  
#  
# Stop, start or restart rTail Server:  
# Just stop, start or restart the rTail Server Docker container  
#  
# Get Shell access to rTail Server Container:  
# $ docker exec -ti rtail-srv bash  
# $ docker exec -ti rtail-srv-nc bash  
# root@3b498458ddfe:/# nc -vv -l -p 8182  
# listening on [any] 8182 ...  
#  
# Send log events to rTail Server Docker Container:  
# You can send any type of log events, from a syslog event, an echo message or
a log by tailing.  
#  
# // Send Ping events to IP addres  
# $ ping 192.168.99.100 | rtail --id pinging --host 192.168.99.100 --port 9191
--mute  
#  
# // Tailing a log file  
# $ tail -f /opt/wiremock/wiremock.log | rtail --id wiremock --host
192.168.99.100 --port 9191 --mute  
#  
  
# Official image: https://hub.docker.com/_/node  
# S.O. Debian 8 - "jessie"  
# 0.12/slim  
FROM node:0.12.9  
  
MAINTAINER Roger CARHUATOCTO <chilcano at intix dot info>  
  
ENV RTAIL_SERVER_PORT_WEB=8181  
ENV RTAIL_SERVER_PORT_UDP=9191  
ENV RTAIL_LISTEN_IP=0.0.0.0  
  
EXPOSE ${RTAIL_SERVER_PORT_WEB} ${RTAIL_SERVER_PORT_UDP} 8182 9192  
  
RUN npm install -g rtail  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
netcat  
RUN apt-get clean && rm -rf /var/cache/apt/* /var/lib/apt/lists/*  
  
CMD rtail-server --wh ${RTAIL_LISTEN_IP} --wp ${RTAIL_SERVER_PORT_WEB} --uh
${RTAIL_LISTEN_IP} --up ${RTAIL_SERVER_PORT_UDP}  

