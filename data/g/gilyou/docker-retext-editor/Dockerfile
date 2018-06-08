FROM ubuntu:bionic  
LABEL org.label-schema.build-date=$BUILD_DATE \  
maintainer="Renwu Gao <gilyou.public@gmail.com>"  
ENV DEBIAN_FRONTEND noninteractive  
ENV LANG=C.UTF-8 \  
LC_ALL=C.UTF-8  
ARG BUILD_DATE  
RUN apt-get update && apt-get install -y \  
wget \  
python3 \  
python3-pyqt5 \  
python3-markups \  
python3-markdown \  
python3-docutils \  
python3-enchant \  
retext \  
xdg-utils \  
fontconfig \  
fonts-wqy-zenhei \  
vim \  
graphviz \  
bzr \  
git \  
locales \  
sudo \  
\--no-install-recommends  
RUN apt-get autoclean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
# Set the locale  
RUN locale-gen zh_CN.UTF-8  
ENV LANG zh_CN.UTF-8  
ENV LANGUAGE zh_CN:zh  
ENV LC_ALL zh_CN.UTF-8  
# Replace 1000 with your user / group id  
RUN export uid=1000 gid=1000 && \  
mkdir -p /home/xiaox && \  
echo "xiaox:x:${uid}:${gid}:xiaox,,,:/home/xiaox:/bin/bash" >> /etc/passwd &&
\  
echo "xiaox:x:${uid}:" >> /etc/group && \  
echo "xiaox ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/xiaox && \  
chmod 0440 /etc/sudoers.d/xiaox && \  
chown ${uid}:${gid} -R /home/xiaox  
  
USER xiaox  
  
WORKDIR /home/xiaox  
CMD [ "retext","--standalone" ]  

