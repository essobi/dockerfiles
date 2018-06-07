FROM frolvlad/alpine-bash  
  
MAINTAINER Jonas Bonno Mikkelsen (https://github.com/JonasBonno)  
  
# Installing dependencies  
RUN apk update && apk add \  
curl \  
git \  
python3-dev \  
ffmpeg \  
opus-dev \  
openssl-dev \  
libffi-dev \  
build-base && \  
rm -rf /var/lib/apt/lists/*  
  
# Installing more dependencies  
RUN curl -k -o /get-pip.py https://bootstrap.pypa.io/get-pip.py  
RUN python3.5 get-pip.py  
RUN pip3 install --upgrade pip  
RUN pip3 install \  
imgurpython \  
youtube_dl  
RUN pip3 install -U
git+https://github.com/Rapptz/discord.py@master\#egg=discord.py[voice]  
RUN git clone -b develop --single-branch https://github.com/Twentysix26/Red-
DiscordBot.git /root/Red-DiscordBot  
  
# Exposes volumes  
VOLUME ["/root/Red-DiscordBot"]  
  
# Setting workdir  
WORKDIR /root/Red-DiscordBot  
  
# Adding startscript and executes it  
ADD start.sh /start.sh  
RUN chmod 0755 /start.sh  
CMD ["bash", "/start.sh"]  

