FROM java:8-jdk  
  
ENV PKG_VER=2018.1.3-no-jdk  
  
RUN apt-get update && \  
apt-get install -y sudo curl sed vim && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/share/intellij && \  
curl --connect-timeout 5 --max-time 600 --retry 5 --retry-delay 0 --retry-max-
time 60 -o /tmp/idea.tar.gz -L
https://download.jetbrains.com/idea/ideaIU-${PKG_VER}.tar.gz && \  
tar -xf /tmp/idea.tar.gz --strip-components=1 -C /usr/share/intellij && \  
rm /tmp/idea.tar.gz  
  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/developer && \  
mkdir -p /home/developer/intellij && \  
if [ -e /usr/share/intellij/bin/idea.properties.orig ] ; then \  
cp /usr/share/intellij/bin/idea.properties.orig
/usr/share/intellij/bin/idea.properties ; \  
else \  
cp /usr/share/intellij/bin/idea.properties
/usr/share/intellij/bin/idea.properties.orig ; \  
fi && \  
sed -i 's~#
idea.config.path=\${user.home}/.IntelliJIdea/config~idea.config.path=/home/developer/intellij/.IntelliJIdea/config~g'
/usr/share/intellij/bin/idea.properties && \  
sed -i 's~#
idea.system.path=\${user.home}/.IntelliJIdea/system~idea.system.path=/home/developer/intellij/.IntelliJIdea/system~g'
/usr/share/intellij/bin/idea.properties && \  
sed -i 's~#idea.true.smooth.scrolling=true~idea.true.smooth.scrolling=true~g'
/usr/share/intellij/bin/idea.properties && \  
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:${uid}:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \  
chmod 0440 /etc/sudoers.d/developer && \  
chown ${uid}:${gid} -R /home/developer && \  
chown ${uid}:${gid} -R /home/developer/intellij  
  
VOLUME /home/developer/intellij  
  
USER developer  
ENV HOME /home/developer  
CMD /usr/share/intellij/bin/idea.sh

