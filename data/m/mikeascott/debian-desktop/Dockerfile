#  
# Debian Desktop (LXDE) Dockerfile  
#  
# https://github.com/mikeascott/ubuntu-desktop  
#  
FROM debian  
MAINTAINER Mike Scott <mike.scott@sqs.com>  
  
# Install LXDE and vnc.  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
locales \  
vim \  
curl \  
tightvncserver \  
lxde  
  
ENV \  
USER=root \  
LANG=en_GB.UTF-8 \  
LANGUAGE=en_GB:en \  
LC_ALL=en_GB.UTF-8  
  
RUN \  
echo "en_GB.UTF-8 UTF-8" > /etc/locale.gen && locale-gen  
  
WORKDIR /data  
  
CMD ["bash"]  
  
EXPOSE 5901

