#  
# tensorflow Dockerfile  
#  
#  
FROM debian:stretch-slim  
  
MAINTAINER Alex Cai "cyy0523xc@gmail.com"  
# Pick up some TF dependencies  
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \  
&& apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
python \  
python-dev \  
python-pip \  
python-setuptools \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pip install -U pip setuptools \  
&& pip --no-cache-dir install \  
numpy \  
pandas \  
scipy \  
sklearn \  
matplotlib \  
tensorflow  
  
# 解决时区问题  
ENV TZ "Asia/Shanghai"  
# 终端设置  
# 默认值是dumb，这时在终端操作时可能会出现：terminal is not fully functional  
ENV TERM xterm  
  
# 解决时区问题  
ENV TZ "Asia/Shanghai"  

