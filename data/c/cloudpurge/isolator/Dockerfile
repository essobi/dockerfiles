# Firefox over VNC with novnc support  
FROM ubuntu:xenial  
LABEL Anatoly_Litovsky <anatolylit@gmail.com>  
ENV container docker  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get clean && apt-get update  
RUN apt-get install -y x11vnc xvfb tar xdotool wget socat gconf2 xz-utils  
RUN apt-get install -y chromium-browser firefox midori libreoffice okular vlc  
  
#building ksm  
RUN apt-get install -y gcc g++ cmake git curl bzip2  
RUN cd /root; git clone https://github.com/unbrice/ksm_preload.git  
RUN cd /root/ksm_preload; cmake .;make;make install  
RUN rm -rf /root/ksm_preload  
RUN apt-get remove -y gcc g++ cmake git  
  
#xserver  
RUN apt-get install -y xserver-xspice  
  
#pulseaudio  
RUN echo "load-module module-pipe-sink file=/home/cage/music/playback.fifo" >>
/etc/pulse/default.pa  
RUN echo "set-default-sink fifo" >> /etc/pulse/default.pa  
#RUN echo "autospawn=no" >> /etc/pulse/client.conf  
RUN echo "default-sink = fifo_output" >> /etc/pulse/client.conf  
  
#dbus magic  
RUN mkdir -p /var/lib/dbus  
RUN mkdir /var/run/dbus  
RUN dbus-uuidgen > /var/lib/dbus/machine-id  
  
#ports  
EXPOSE 5900  
#prepare locks  
RUN mkdir -p /mnt/locks  
VOLUME /mnt/locks  
RUN mkdir -p /SRV  
  
COPY run.sh /run.sh  
RUN chmod +x run.sh  
  
#creating user  
RUN useradd cage  
RUN mkdir /home/cage  
RUN chown cage:cage /home/cage  
  
COPY spiceqxl.xorg.conf /home/cage/spiceqxl.xorg.conf  
COPY user-run.sh /home/cage/user-run.sh  
COPY AdjustToClosestRes.py /home/cage/AdjustToClosestRes.py  
RUN chown cage:cage /home/cage/*  
  
#restricted from now  
USER cage  
#install tor browser  
RUN cd /home/cage && \  
curl https://dist.torproject.org/torbrowser/7.5.2/tor-browser-
linux64-7.5.2_en-US.tar.xz | \  
tar xvJ  
  
RUN cd /home/cage && chmod +x user-run.sh  
  
#fix chrome  
RUN mkdir -p /home/cage/.config/chromium  
RUN touch "/home/cage/.config/chromium/First Run"  
#add spice config  
# go  
USER root  
CMD ["/run.sh"]  

