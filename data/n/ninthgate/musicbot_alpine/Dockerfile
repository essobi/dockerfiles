FROM alpine:3.5  
#ypdate 10-02-17  
MAINTAINER Sidesplitter, https://github.com/SexualRhinoceros/MusicBot  
MAINTAINER dzirtt, https://github.com/dzirtt/musicBot_alpine  
  
##Install dependencies  
#donwload  
RUN apk add --update wget unzip libcurl git  
#musicbot deps  
RUN apk add python3 python3-dev ffmpeg opus-dev  
#compilation  
RUN apk add gcc make libc-dev binutils libffi-dev  
  
#Install Pip  
#RUN wget https://bootstrap.pypa.io/get-pip.py \  
# && python3.5 get-pip.py  
#Install PIP dependencies from requirements.txt  
#--trusted-host pypi.python.org becose of error with SSL cert  
#more here https://github.com/pypa/pip/issues/4205  
RUN python3 -m pip install discord.py[voice] \  
youtube_dl \  
pip  
  
#download musicBot  
RUN git clone -b master --single-branch
https://github.com/SexualRhinoceros/MusicBot.git /musicBot  
WORKDIR /musicBot  
  
#cleanup  
RUN apk del gcc make git && \  
rm -rf /var/lib/apt/lists/*  
  
#Add volume for configuration  
VOLUME /musicBot/config  
  
CMD python3 run.py  

