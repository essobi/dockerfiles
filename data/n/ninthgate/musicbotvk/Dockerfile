FROM alpine:latest  
  
#update 10-02-17  
MAINTAINER Sidesplitter, https://github.com/SexualRhinoceros/MusicBot  
MAINTAINER dzirtt, https://github.com/dzirtt/musicBot_alpine  
  
##Install dependencies  
#donwload, unpack  
RUN apk add --update wget unzip libcurl git  
#musicbot deps  
RUN apk add python3 python3-dev ffmpeg opus-dev  
#compilation  
RUN apk add gcc make libc-dev binutils libffi-dev  
  
#Install Pip  
RUN wget https://bootstrap.pypa.io/get-pip.py \  
&& python3.5 get-pip.py  
  
#Install PIP dependencies from requirements.txt  
RUN pip install discord.py[voice] \  
youtube_dl \  
pip \  
vk  
  
#download musicBot  
RUN git clone -b master --single-branch https://github.com/dzirtt/MusicBot.git
/musicBot  
WORKDIR /musicBot  
  
#cleanup  
RUN apk del gcc make git && \  
rm -rf /var/lib/apt/lists/*  
  
#Add volume for configuration  
VOLUME /musicBot/config  
  
CMD python3.5 run.py  

