FROM ubuntu:16.04  
  
MAINTAINER Furious George <furiousgeorgecode@gmail.com>  
# More SSL cert problems on automatic build on Docker hub:  
ENV GIT_SSL_NO_VERIFY true  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV APTLIST="git libav-tools libffi-dev libopus-dev libssl-dev python3.5-dev
unzip ffmpeg wget ca-certificates build-essential"  
ENV
PIPLIST="git+https://github.com/Rapptz/discord.py@master#egg=discord.py[voice]
imgurpython youtube_dl beautifulsoup4"  
RUN apt-get update && apt-get install -y \--no-install-recommends $APTLIST &&
apt-get clean  
RUN ln -s /usr/bin/python3.5 /usr/bin/python  
# Keep getting certificate errors when Docker Hub is building this image -
added -no-check-certificate  
RUN wget \--no-check-certificate -O /tmp/get-pip.py
http://bootstrap.pypa.io/get-pip.py && python3.5 /tmp/get-pip.py  
RUN pip install \--trusted-host pypi.python.org $PIPLIST  
  
RUN git clone -b develop \--single-branch https://github.com/Twentysix26/Red-
DiscordBot.git /app  
  
VOLUME /app/data  
WORKDIR /app  
  
CMD ["python", "./red.py", "--no-prompt"]  

