FROM debian:jessie  
  
ENV UPDATE yes  
ENV VNCPASS jriver  
ENV MONITOR :1  
# Install wget  
RUN apt-get update \  
&& apt-get install -y wget \  
  
# Add JRiver packages to apt-get  
&& wget -q "http://dist.jriver.com/mediacenter@jriver.com.gpg.key" -O- | apt-
key add \- \  
&& wget http://dist.jriver.com/stable/mediacenter/mediacenter22jessie.list -O
\  
/etc/apt/sources.list.d/mediacenter22.list \  
  
# Install JRiver and other required apps  
&& apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
mediacenter22 \  
supervisor \  
xserver-xorg-video-dummy \  
x11vnc \  
&& rm -rf /var/lib/apt/lists/*  
  
# Add config files  
COPY xorg.conf /etc/X11/  
COPY entrypoint.sh /usr/local/bin/  
COPY supervisord.conf /etc/supervisor/conf.d/  
  
# Set files access permissions  
RUN chmod 744 /etc/X11/xorg.conf \  
&& chmod 700 /usr/local/bin/entrypoint.sh \  
&& chmod 700 /etc/supervisor/conf.d/supervisord.conf \  
  
# Add user and group  
&& groupadd -r jriver \  
&& useradd -r -ms /bin/bash -g jriver jriver \  
  
# Set up VNC  
&& mkdir /home/jriver/.vnc \  
&& chown jriver:jriver /home/jriver/.vnc \  
  
# Set up JRiver  
&& mkdir /home/jriver/.jriver \  
&& chown jriver:jriver /home/jriver/.jriver  
VOLUME ["/home/jriver/.jriver"]  
  
EXPOSE 5900 52100 52101 52199 1900/udp  
  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  

