FROM ubuntu:xenial  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN echo '\n\  
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted
universe multiverse\n\  
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted
universe multiverse\n\  
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main
restricted universe multiverse\n\  
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main
restricted universe multiverse\n\  
' > /etc/apt/sources.list  
  
RUN apt update  
# language-pack-zh-hans  
RUN apt install -y --no-install-recommends locales dbus-x11 gnome-terminal  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV NO_AT_BRIDGE 1  
RUN mkdir -p ~/.pip && echo '[global]\n\  
index-url=https://pypi.tuna.tsinghua.edu.cn/simple' > ~/.pip/pip.conf  
  
RUN apt install -y --no-install-recommends python-pip python3-pip  
RUN python2 -m pip install --upgrade pip  
RUN python3 -m pip install --upgrade pip  
RUN pip2 install setuptools  
RUN pip3 install setuptools  
  

