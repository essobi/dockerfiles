FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo 'apt-get update -qq && apt-get install -yq $@ && apt-get clean && rm
-rf /var/lib/apt/lists/*' > /usr/local/bin/aptget.sh &&\  
chmod +x /usr/local/bin/aptget.sh  
  
# japanize  
RUN \  
# set timezone  
ln -s -f /usr/share/zoneinfo/Asia/Tokyo /etc/localtime &&\  
dpkg-reconfigure tzdata &&\  
aptget.sh fonts-takao sudo &&\  
# generate locale  
locale-gen ja_JP.UTF-8  
ENV LANG ja_JP.UTF-8  
# create user vagrant. uid:gid=1000:1000  
ENV USER vagrant  
ENV HOME /home/${USER}  
RUN export uid=1000 gid=1000 &&\  
echo "${USER}:x:${uid}:${gid}:Developer,,,:${HOME}:/bin/bash" >> /etc/passwd
&&\  
echo "${USER}:x:${uid}:" >> /etc/group &&\  
echo "${USER} ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers &&\  
install -d -m 0755 -o ${uid} -g ${gid} ${HOME}  
WORKDIR ${HOME}  
  
# X  
ENV DISPLAY :0.0  
VOLUME /tmp/.X11-unix  
VOLUME ${HOME}  
USER ${USER}  
  
# add packages  
# RUN sudo aptget.sh firefox  
#CMD /usr/bin/firefox  

