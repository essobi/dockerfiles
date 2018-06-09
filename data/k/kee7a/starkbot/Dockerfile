FROM alpine:latest  
MAINTAINER Jeff Siqueira <root@kee7a.com>  
  
RUN apk add --update python3 git && rm -rf /var/cache/apk/*  
  
RUN pip3 install discord.py && \  
rm -rf \  
/root/.cache/pip  
  
RUN addgroup \  
-S -g 1000 \  
bot && \  
adduser \  
-S -H -D \  
-h /data \  
-s /bin/sh \  
-u 1000 \  
-G bot \  
bot  
  
RUN mkdir /data  
RUN chown bot:bot /data  
USER bot  
  
  
WORKDIR /data  
RUN git clone http://git.josh951623.tech/josh951623/StarkRavingPythonBot.git  
VOLUME ["/data/StarkRavingPythonBot/vars.py"]  
ENTRYPOINT ["/usr/bin/python3","/data/StarkRavingPythonBot/start.py"]  
  
#docker run --name starkbot -v
path/to/vars.py:/data/StarkRavingPythonBot/vars.py -d kee7a/starkbot:0.1-a  

