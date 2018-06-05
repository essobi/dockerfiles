FROM konstruktoid/alpine  
  
LABEL org.label-schema.name="aether" \  
org.label-schema.vcs-url="git://github.com/konstruktoid/Aether_Build.git"  
  
ENV DL 'https://github.com/nehbit/aether-public/releases/download/v1.2.3-LNX-
TAR/aether_1.2.3.tar.bz2'  
ENV USER aether  
ENV HOME /home/$USER  
RUN \  
apk update && \  
apk upgrade && \  
rm -rf /var/cache/apk/*  
  
RUN \  
adduser -D -h $HOME -s /bin/sh $USER && \  
mkdir -p $HOME/.config/autostart && \  
chown -R $USER:$USER $HOME  
  
RUN \  
echo "NOTE: This version of Aether (V1) is currently deprecated." && \  
wget -qO /tmp/aether.tar.bz2 $DL && \  
tar -xjvf /tmp/aether.tar.bz2 -C /usr/local/bin && \  
rm /tmp/aether.tar.bz2  
  
WORKDIR $HOME  
USER aether  
  
ENTRYPOINT ["/usr/local/bin/aether/Aether"]  
CMD [""]  

