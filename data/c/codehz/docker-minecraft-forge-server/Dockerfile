FROM java:7-jre  
  
MAINTAINER Nicolas FAVRE & Dot Back  
  
ENV MCSERVER_PATH /srv/minecraft  
  
  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4  
RUN apt-get update && apt-get install -y curl screen && rm -rf
/var/lib/apt/lists/* \  
&& curl -o /usr/local/bin/gosu -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture)" \  
&& curl -o /usr/local/bin/gosu.asc -SL
"https://github.com/tianon/gosu/releases/download/1.2/gosu-$(dpkg --print-
architecture).asc" \  
&& gpg --verify /usr/local/bin/gosu.asc \  
&& rm /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu  
  
RUN \  
groupadd -g 1000 minecraft && \  
useradd -g minecraft -u 1000 -r -M minecraft  
  
RUN mkdir -p $MCSERVER_PATH  
  
VOLUME ["$MCSERVER_PATH"]  
  
WORKDIR $MCSERVER_PATH  
  
COPY minecraft /usr/local/bin/  
RUN chmod +x /usr/local/bin/minecraft  
  
EXPOSE 25565  
EXPOSE 25575  
CMD ["minecraft", "run"]

