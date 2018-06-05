FROM ubuntu  
  
ENV container docker  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN sed -i -E 's!archive.ubuntu.com!mirrors.aliyun.com!' /etc/apt/sources.list  
RUN sed -i -E 's!security.ubuntu.com!mirrors.aliyun.com!'
/etc/apt/sources.list  
  
RUN apt-get update && apt-get install -y openssh-client vim htop tmux build-
essential && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /root  
  
ADD dummy-init.c /tmp  
  
RUN gcc /tmp/dummy-init.c -O3 -s -DNDEBUG -o /usr/bin/dummy-init  
  
CMD ["/usr/bin/dummy-init"]  

