FROM vbaruh/firefox32-base  
  
# add infonotary repo into apt sources  
# bit4id package is in this repo  
run wget
http://repository.infonotary.com/install/linux/INotaryCodeSigning.key.asc \  
&& apt-key add INotaryCodeSigning.key.asc \  
&& wget -P /etc/apt/sources.list.d
http://repository.infonotary.com/install/linux/infonotary.list  
  
# install all necessary packages  
# usbutils is used only for debugging purposes  
run apt-get update \  
&& apt-get install -y \  
pcscd \  
libacr38u \  
bit4id-ipki \  
unzip \  
usbutils  
  
# download and install infonotary's plugin which configures firefox to use the
smart card  
run wget -O infonotary.xpi
https://addons.mozilla.org/firefox/downloads/file/258086/infonotary_configurator_for_mozilla-1.4.4-fx+tb+sm+fn-
linux.xpi?src=dp-btn-primary \  
&& mkdir -p /opt/firefox/browser/extensions/infonotary-mozilla-
setup@infonotary.com \  
&& cd /opt/firefox/browser/extensions/infonotary-mozilla-setup@infonotary.com
\  
&& unzip /infonotary.xpi  
  
# initialize firefox user - home dir, permissions, etc  
run export uid=1000 gid=1000 && \  
mkdir -p /home/firefox && \  
echo "firefox:x:${uid}:${gid}:firefox,,,:/home/firefox:/bin/bash" >>
/etc/passwd && \  
echo "firefox:x:${uid}:" >> /etc/group && \  
echo "firefox ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/firefox && \  
chmod 0440 /etc/sudoers.d/firefox && \  
chown ${uid}:${gid} -R /home/firefox  
  
# act as firefox  
USER firefox  
ENV HOME /home/firefox  
  
# export home directory as volume  
VOLUME /home/firefox  
  
# start pcscd service and then firefox  
CMD sudo /etc/init.d/pcscd start && /usr/bin/firefox  

