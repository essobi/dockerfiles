FROM i386/alpine:3.4  
RUN adduser -S sharptalk  
  
RUN apk update && apk add --no-cache \  
curl \  
xvfb  
  
RUN apk add --no-cache \  
\--repository https://dl-3.alpinelinux.org/alpine/edge/community/ \  
wine=2.0.2-r0  
  
COPY bin/winetricks /usr/local/bin/  
  
RUN mkdir -p /usr/share/wine/mono/ && cd /usr/share/wine/mono/ \  
&& curl -O https://dl.winehq.org/wine/wine-mono/4.6.4/wine-mono-4.6.4.msi \  
&& chown -R sharptalk .  
  
USER sharptalk  
ENV WINEPREFIX /home/sharptalk/.wine  
ENV WINEARCH win32  
# Silence all the "fixme: blah blah blah" messages from wine  
ENV WINEDEBUG fixme-all  
ENV DISPLAY :0  
WORKDIR /home/sharptalk  
  
RUN wineboot --init \  
&& while pgrep wineserver >/dev/null; do echo "Waiting for wineserver"; sleep
1; done \  
&& rm /usr/share/wine/mono/*.msi  
  
COPY lib lib  
COPY .asoundrc .  
COPY bin/run.sh .  
  
ENTRYPOINT ["./run.sh"]  

