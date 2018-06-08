FROM ubuntu:yakkety  
MAINTAINER Calvin Nguyen <calvin4084@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
ca-certificates \  
bash \  
bash-completion \  
ncurses-base \  
vim \  
curl \  
procps && \  
dpkg --add-architecture i386 &&\  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ADD rootfs /  
  
ENV CRON_ENABLED false  
ENV TERM xterm  
CMD ["bash"]  

