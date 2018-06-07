FROM alpine  
  
MAINTAINER Adrian Noss (adrian.noss@gmail.com)  
  
# install needed apks  
RUN apk update && \  
apk add \  
git \  
python3-dev \  
ffmpeg \  
opus-dev \  
openssl-dev \  
libffi-dev \  
build-base && \  
rm -rf /var/lib/apt/lists/*  
  
# get python 3 pip version  
RUN wget https://bootstrap.pypa.io/get-pip.py  
RUN python3 get-pip.py  
  
# install needed modules from pip  
RUN pip install \  
beautifulsoup4 \  
imgurpython \  
youtube_dl \  
git+https://github.com/Rapptz/discord.py@async  
  
# git clone red bot  
RUN git clone -b develop --single-branch https://github.com/Twentysix26/Red-
DiscordBot.git /app  
  
# set volume and workdir  
VOLUME /app/data  
WORKDIR /app  
  
# start command red bot  
CMD ["python3", "./red.py"]  

