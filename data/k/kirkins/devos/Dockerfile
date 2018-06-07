FROM ubuntu:16.04  
MAINTAINER Paimpozhil "paimpozhil@gmail.com"  
RUN apt-get update  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get install -y openssh-server xubuntu-desktop  
  
RUN add-apt-repository ppa:x2go/stable  
  
RUN apt-get update  
  
RUN apt-get install x2goserver x2goserver-xsession pwgen -y  
  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config  
RUN sed -i "s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
RUN sed -i "s/#PasswordAuthentication/PasswordAuthentication/g"
/etc/ssh/sshd_config  
  
RUN mkdir -p /tmp/.X11-unix && chmod 1777 /tmp/.X11-unix  
  
ADD set_root_pw.sh /set_root_pw.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
EXPOSE 22  
CMD ["sudo /run.sh"]  
  
# Create a new user account with UID/GID at least 10000.  
# This makes it easier to keep host and docker accounts apart.  
RUN useradd --home /var/subsonic -M subsonic -K UID_MIN=10000 -K GID_MIN=10000
&& \  
mkdir -p /var/subsonic && chown subsonic /var/subsonic && chmod 0770
/var/subsonic  
  
RUN sudo add-apt-repository ppa:openjdk-r/ppa  
  
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && \  
apt-get update && \  
apt-get dist-upgrade --yes --no-install-recommends --no-install-suggests && \  
apt-get install --yes --no-install-recommends --no-install-suggests
openjdk-7-jre-headless locales && \  
apt-get clean  
  
ENV SUBSONIC_VERSION 6.0  
ADD
http://downloads.sourceforge.net/project/subsonic/subsonic/$SUBSONIC_VERSION/subsonic-$SUBSONIC_VERSION.deb?r=http%3A%2F%2Fsourceforge.net%2Fprojects%2Fsubsonic%2Ffiles%2Fsubsonic%2F$SUBSONIC_VERSION%2F&ts=1421842428&use_mirror=optimate
/tmp/subsonic-$SUBSONIC_VERSION.deb  
RUN dpkg -i /tmp/subsonic-$SUBSONIC_VERSION.deb && rm -f /tmp/*.deb  
  
# Create hardlinks to the transcoding binaries.  
# This way we can mount a volume over /var/subsonic.  
# Apparently, Subsonic does not accept paths in the Transcoding settings.  
# If you mount a volume over /var/subsonic, create symlinks  
# <host-dir>/var/subsonic/transcode/ffmpeg -> /usr/local/bin/ffmpeg  
# <host-dir>/var/subsonic/transcode/lame -> /usr/local/bin/lame  
RUN ln /var/subsonic/transcode/ffmpeg /var/subsonic/transcode/lame
/usr/local/bin  
  
VOLUME /var/subsonic  
  
COPY startup.sh /startup.sh  
  
EXPOSE 4040  
USER subsonic  
  
CMD []  
ENTRYPOINT ["/startup.sh"]  

