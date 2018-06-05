FROM martinjohn/rclone:beta  
  
RUN set -x \  
&& apk update \  
&& apk --no-cache add \  
firefox-esr \  
xfce4 \  
xfce4-terminal \  
xvfb \  
&& apk --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing
add \  
x11vnc \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /docker  
ADD start.sh /docker  
RUN chmod 755 /docker/start.sh  
  
ADD xfce4-panel.xml /root/.config/xfce4/xfconf/xfce-perchannel-
xml/xfce4-panel.xml  
  
EXPOSE 5900  
VOLUME /data  
ENV VNC_RESOLUTION="800x600"  
ENTRYPOINT ["/bin/ash"]  
CMD ["/docker/start.sh"]  

