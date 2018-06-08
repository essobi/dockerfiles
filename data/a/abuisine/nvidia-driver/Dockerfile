FROM ubuntu:17.04  
LABEL maintainer="Alexandre Buisine <alexandrejabuisine@gmail.com"  
LABEL version="375.66-2"  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq update \  
&& apt-get install -yqq --no-install-recommends \  
module-init-tools \  
make \  
gcc \  
sysdig-dkms \  
&& apt-get -yqq clean \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV NVIDIA_DRIVER_VERSION="375.66"  
WORKDIR /home/nvidia  
COPY resources/NVIDIA-Linux-x86_64-${NVIDIA_DRIVER_VERSION}.run .  
COPY resources/docker-entrypoint.sh /usr/local/sbin/  
  
RUN chmod +x /usr/local/sbin/docker-entrypoint.sh /home/nvidia/NVIDIA-
Linux-x86_64-${NVIDIA_DRIVER_VERSION}.run  
  
ENTRYPOINT [ "/usr/local/sbin/docker-entrypoint.sh" ]  
CMD [ "--ui=none", "--accept-license", "--no-questions", "--dkms" ]

