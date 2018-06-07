FROM alpine:latest  
  
MAINTAINER jbltx <gtmicka@hotmail.fr>  
  
ENV OWNER_ID 1234  
ENV COMMAND_PREFIX .  
ENV DISCORD_TOKEN 1234  
ENV ADMINS_NAME Admins  
ENV MODS_NAME Mods  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && apk update && apk upgrade && \  
mkdir -p /opt/app-root/src && \  
apk add --update python3 python3-dev build-base libffi-dev ffmpeg opus git
geos  
  
COPY . /opt/app-root/src/  
  
RUN pip3 install --upgrade pip && pip3 install --upgrade -r /opt/app-
root/src/requirements.txt && chmod -R 777 /opt/app-root/src  
  
WORKDIR /opt/app-root/src  
  
ENTRYPOINT ["/opt/app-root/src/start.sh"]  
  
CMD ["--auto-restart"]  

