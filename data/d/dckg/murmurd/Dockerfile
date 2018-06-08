FROM debian:jessie  
  
MAINTAINER David Gressel <dckgdotnet@gmail.com> (https://dckg.net
https://github.com/dckg)  
  
RUN apt-get update && \  
apt-get install -y \  
mumble-server && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ./docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENV SERVER_PASSWORD=${SERVER_PASSWORD:-""}  
ENV BANDWIDTH=${BANDWIDTH:-72000}  
ENV USERS=${USERS:-100}  
ENV WELCOMETEXT=${WELCOMETEXT:-"Welcome to this dockerized mumble-server
instance powered by <a href=\"https://dckg.net\">dckg.net</a>"}  
ENV SUPERUSER_PASSWORD=${SUPERUSER_PASSWORD}  
  
EXPOSE 64738/udp  
  
VOLUME /data  
  
ENTRYPOINT ["/docker-entrypoint.sh"]

