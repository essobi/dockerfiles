FROM ubuntu:zesty  
  
RUN apt update  
  
RUN apt install -y libgl1-mesa-glx libqt5widgets5 wget  
  
RUN useradd -ms /bin/bash tes3mp  
  
USER tes3mp  
  
WORKDIR /home/tes3mp  
  
RUN wget https://github.com/TES3MP/openmw-
tes3mp/releases/download/tes3mp-0.6.1/tes3mp-
GNU.Linux-x86_64-release-0.6.1-f532ab241d-p7.tar.gz  
  
RUN tar -xzf *.tar.gz  
  
RUN mkdir -p ~/.config/ && mkdir -p ~/.local/share/ && rm
/home/tes3mp/TES3MP/tes3mp-server-default.cfg  
  
USER root  
  
RUN mkdir /data  
  
RUN ln -s /data/tes3mp-server-default.cfg /home/tes3mp/TES3MP/tes3mp-server-
default.cfg && \  
ln -s /data/config /home/tes3mp/.config/openmw && \  
ln -s /data/share /home/tes3mp/.local/share/openmw  
  
# TCP optional?  
EXPOSE 25565/udp  
  
# Set up core dumps  
RUN echo '* soft core unlimited' >> /etc/security/limits.conf  
RUN echo '* hard core unlimited' >> /etc/security/limits.conf  
  
# Requires --privileged :(  
# RUN echo '/data/core.%e.%p.%t' > /proc/sys/kernel/core_pattern  
USER tes3mp  
  
ENTRYPOINT ["/home/tes3mp/TES3MP/tes3mp-server"]  

