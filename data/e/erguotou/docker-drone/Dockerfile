FROM ubuntu  
MAINTAINER erguotou525@gmail.com  
RUN \  
apt-get update -y \  
&& apt-get install wget libsqlite3-dev -y \  
&& wget -qO- https://get.docker.com/ | sh \  
&& wget downloads.drone.io/master/drone.deb \  
&& dpkg -i drone.deb  
  
EXPOSE 80  
VOLUME /var/lib/docker  
VOLUME /var/lib/drone  
  
ENV DRONE_SERVER_PORT :80  
ENV DRONE_DATABASE_DATASOURCE /var/lib/drone/drone.sqlite3  
  
CMD service docker start &&/user/local/bin/droned  

