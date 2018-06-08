FROM ubuntu:14.04  
MAINTAINER Study Hsueh <ph.study@gmail.com>  
  
RUN apt-get update -q  
RUN apt-get install -qy make gcc libmysqlclient-dev zlib1g-dev libpcre3-dev
mysql-client curl  
  
ADD . /rAthena  
  
WORKDIR /rAthena  
  
# Configure and compile  
RUN cd /rAthena && ./configure && make clean && make sql  
  
RUN sed -i "s|//login_ip:|login_ip:|g" /rAthena/conf/char_athena.conf \  
&& sed -i "s|//char_ip:|char_ip:|g" /rAthena/conf/char_athena.conf \  
&& sed -i "s|//char_ip:|char_ip:|g" /rAthena/conf/map_athena.conf \  
&& sed -i "s|//map_ip:|map_ip:|g" /rAthena/conf/map_athena.conf  
  
ENTRYPOINT ["/rAthena/docker-entrypoint.sh"]  
  
EXPOSE 6900/tcp 6121/tcp 5121/tcp  
  
CMD ["/rAthena/athena-start", "watch"]  

