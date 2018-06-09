FROM debian:latest  
  
RUN apt-get update && apt-get install -y \  
build-essential \  
curl \  
tar \  
bzip2 \  
libmariadb2 \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV TSPK_VERSION 3.0.13.6  
ENV TSPK_DOWNLOAD_URL
http://dl.4players.de/ts/releases/$TSPK_VERSION/teamspeak3-server_linux_amd64-$TSPK_VERSION.tar.bz2  
ENV TSPK_DOWNLOAD_SHA256
19ccd8db5427758d972a864b70d4a1263ebb9628fcc42c3de75ba87de105d179  
  
COPY ./initscript /usr/local/initscript  
RUN chmod 755 /usr/local/initscript  
  
RUN curl -fsSL "$TSPK_DOWNLOAD_URL" -o teamspeak3.tar.bz2 \  
&& echo "$TSPK_DOWNLOAD_SHA256 teamspeak3.tar.bz2" | sha256sum -c - \  
&& tar -C /usr/local -jxf teamspeak3.tar.bz2 \  
&& rm teamspeak3.tar.bz2  
  
COPY ./ts3server.ini /usr/local/teamspeak3-server_linux_amd64/ts3server.ini  
COPY ./ts3db_mariadb.ini
/usr/local/teamspeak3-server_linux_amd64/ts3db_mariadb.ini  
  
EXPOSE 9987 10011 30033  
CMD ["/usr/local/initscript"]  
  
# docker run -d --name=teamspeak --restart=unless-stopped -p 9987:9987/udp -p
10011:10011 -p 30033:30033 onzeway/teamspeak_server_docker:latest

