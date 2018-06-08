FROM ubuntu:16.04  
LABEL maintainer="david@cninone.com"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV LANG en_US.UTF-8  
ENV LC_ALL "C.UTF-8"  
ENV LANGUAGE en_US:en  
COPY sources.list /etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y --fix-missing \  
build-essential \  
cmake \  
gfortran \  
git \  
wget \  
curl \  
graphicsmagick \  
libgraphicsmagick1-dev \  
libatlas-dev \  
libavcodec-dev \  
libavformat-dev \  
libgtk2.0-dev \  
libjpeg-dev \  
liblapack-dev \  
libswscale-dev \  
pkg-config \  
python-dev \  
python-numpy \  
sudo \  
python \  
python-pip \  
pkg-config \  
software-properties-common \  
zip \  
wget \  
supervisor \  
openssh-server \  
net-tools tzdata language-pack-en-base \  
lsof initramfs-tools upstart-sysv \  
&& update-initramfs -u \  
&& apt-get purge systemd -y \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
  
RUN mkdir -p /var/log/supervisor /var/log/nginx /var/run/sshd /data/apps  
  
RUN useradd -ms /bin/bash david && usermod -aG sudo david  
RUN echo 'david:freego' | chpasswd  
RUN echo 'root:freego_2018' | chpasswd  
# RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile \  
&& echo "/var/www *(rw,async,no_subtree_check,insecure)" >> /etc/exports \  
&& echo "export TERM=xterm" >> ~/.bashrc  
ENV TZ=Asia/Chongqing  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN pip install --upgrade pip && pip install opencv-python pymongo eventlet
flask flask_socketio pydash face_recognition  
# WORKDIR /root/openface  
WORKDIR /data/apps  
EXPOSE 22 1979  
ADD ./svr/ /data/apps  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]

