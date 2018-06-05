FROM alpine:3.7  
RUN apk add --no-cache unzip  
  
WORKDIR /tmp  
COPY jalinuxded_1011.zip jalinuxded_1011.zip  
RUN unzip -d jedi_academy/ jalinuxded_1011.zip  
  
FROM debian:9-slim  
MAINTAINER McAfee  
  
# requires the lib32 libraries  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y lib32stdc++6 && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /files && \  
mkdir -p /usr/local/games/ja/ && \  
ln -s /files /usr/local/games/ja/base  
  
# main program  
COPY \--from=0 /tmp/jedi_academy/libcxa.so.1 /usr/lib/libcxa.so.1  
COPY \--from=0 /tmp/jedi_academy/linuxjampded /usr/local/games/ja/linuxjampded  
  
# default unmodded files  
COPY \--from=0 /tmp/jedi_academy/jampgamei386.so /tmp/jampgamei386.so  
COPY \--from=0 /tmp/jedi_academy/server.cfg /tmp/server.cfg  
  
RUN chmod a+x /usr/local/games/ja/linuxjampded && \  
chmod a+x /usr/lib/libcxa.so.1  
  
COPY run.sh /usr/local/games/ja/run.sh  
  
RUN chmod a+x /usr/local/games/ja/run.sh  
  
VOLUME /files  
WORKDIR /usr/local/games/ja/  
CMD ./run.sh  
  

