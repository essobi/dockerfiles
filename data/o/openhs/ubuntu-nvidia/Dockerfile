# Dockerfile  
#  
# Project: docker-ubuntu-nvidia  
# License: GNU GPLv3  
#  
# Copyright (C) 2015 - 2016 Robert Cernansky  
FROM openhs/ubuntu-x  
  
  
  
MAINTAINER openhs  
LABEL version = "0.5.0" \  
description = "Base Ubuntu image with nVidia graphics driver."  
  
ARG default_nvidia_version=361  
ENV NVIDIA_DRIVER_VERSION=${default_nvidia_version}  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
nvidia-${default_nvidia_version} \  
# nvidia depends on initramfs-tools  
initramfs-tools  
  
COPY select_nvidia_driver.sh add_user_to_video_group.sh docker-ubuntu-
nvidia_startup.sh /opt/  
RUN chmod +x /opt/select_nvidia_driver.sh /opt/add_user_to_video_group.sh
/opt/docker-ubuntu-nvidia_startup.sh  
  
ENTRYPOINT ["/opt/docker-ubuntu-nvidia_startup.sh"]  

