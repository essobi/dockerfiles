FROM "resin/armv7hf-debian:stretch"  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV USER pulseaudio  
ENV UID 1000  
ENV HOSTPULSE 116  
ENV GROUPS audio,hostpulse  
ENV HOME /home/$USER  
RUN [ "cross-build-start" ]  
  
RUN apt-get update \  
&& apt-get install -yq pulseaudio \  
&& rm -rf /var/lib/apt/lists  
  
COPY [ "default.pa", "client.conf", "daemon.conf", "/etc/pulse/" ]  
  
RUN groupadd -g $HOSTPULSE hostpulse  
RUN useradd -u $UID -m -d $HOME -s /usr/sbin/nologin $USER \  
&& usermod -aG $GROUPS $USER \  
&& chmod 0644 -- /etc/pulse/* \  
&& mkdir -p $HOME/.config/pulse \  
&& chown -Rh $USER:$USER \-- $HOME  
  
RUN [ "cross-build-end" ]  
  
WORKDIR $HOME  
USER $USER  
VOLUME [ "/tmp", "$HOME/.config/pulse" ]  
ENTRYPOINT [ "/usr/bin/pulseaudio" ]  

