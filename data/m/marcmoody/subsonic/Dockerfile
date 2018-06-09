FROM ubuntu:trusty  
RUN locale-gen en_US.UTF-8  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository ppa:mc3man/trusty-media && \  
apt-get update && \  
apt-get install openjdk-7-jre-headless wget ffmpeg -y && \  
apt-get install -y lame  
  
RUN groupadd subsonic && \  
useradd -r -g subsonic -s /sbin/nologin -c "Subsonic user" subsonic  
RUN mkdir -p /opt/subsonic && chown subsonic:subsonic /opt/subsonic && \  
mkdir -p /var/subsonic/transcode && chown -R subsonic:subsonic /var/subsonic  
  
RUN ln -s /usr/bin/ffmpeg /var/subsonic/transcode/ffmpeg && \  
ln -s /usr/bin/lame /var/subsonic/transcode/lame  
  
ENV SUBSONIC_VERSION 5.2.1  
RUN wget -qO-
http://downloads.sourceforge.net/project/subsonic/subsonic/$SUBSONIC_VERSION/subsonic-$SUBSONIC_VERSION-
standalone.tar.gz | tar xvz -C /opt/subsonic  
  
RUN sed -i "s/ > \${LOG} 2>&1 &//" /opt/subsonic/subsonic.sh  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
VOLUME ["/var/subsonic"]  
  
ENTRYPOINT ["/opt/subsonic/subsonic.sh"]  
  
EXPOSE 4040  
EXPOSE 4443  

