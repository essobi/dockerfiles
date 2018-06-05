FROM alpine:latest  
  
MAINTAINER Sidesplitter, https://github.com/SexualRhinoceros/MusicBot  
MAINTAINER dzirtt, https://github.com/dzirtt/musicBot_alpine  
MAINTAINER Omar007, https://github.com/Omar007/Docker-DiscordMusicBot/  
  
##Install dependencies  
#download  
RUN apk add --update wget unzip libcurl git  
#musicbot deps  
RUN apk add python3 python3-dev ffmpeg opus-dev  
#compilation  
RUN apk add gcc make libc-dev binutils libffi-dev  
  
#Install Pip  
RUN wget https://bootstrap.pypa.io/get-pip.py \  
&& python3.5 get-pip.py  
  
#download musicBot  
RUN git clone -b review --single-branch https://github.com/Just-Some-
Bots/MusicBot.git /musicBot  
WORKDIR /musicBot  
  
#install pip dependencies  
RUN pip install -r requirements.txt  
  
#cleanup  
RUN apk del gcc make git \  
&& rm -rf /var/lib/apt/lists/*  
  
#Add volume for configuration  
VOLUME /musicBot/config  
  
CMD python3.5 run.py  

