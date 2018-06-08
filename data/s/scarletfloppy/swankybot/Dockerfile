FROM resin/rpi-raspbian:stretch  
MAINTAINER ScarletFloppy  
ENV name SwankyBot  
ENV token null  
RUN [ "cross-build-start" ]  
RUN apt update \  
&& apt install python3 python3-wheel python3-pip wget unzip \  
&& pip3 install --upgrade pip setuptools \  
&& pip3 install --upgrade python-telegram-bot \  
&& wget -O /tmp/master.zip
https://github.com/ScarletFloppy/${name}/archive/master.zip \  
&& mkdir -p /bot \  
&& unzip -d /bot /tmp/master.zip \  
&& rm /tmp/master.zip  
RUN [ "cross-build-end" ]  
ENTRYPOINT sh -c "python3 /bot/${name}-master/bot.py ${token}"  

