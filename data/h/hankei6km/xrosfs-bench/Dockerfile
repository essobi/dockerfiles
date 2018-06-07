FROM debian:stretch-slim  
# test bench image(sshfs server)  
ENV LANG C.UTF-8  
ARG USER=pdu  
  
# Install and setup sshd.  
# https://hub.docker.com/r/rastasheep/ubuntu-sshd/~/dockerfile/  
RUN apt-get update && apt-get upgrade -y \  
&& apt-get install -y --no-install-recommends \  
openssh-server \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/run/sshd  
  
RUN echo 'root:root' |chpasswd  
  
# `PermitRootLogin` line comment outed of debian strech.  
RUN sed -ri 's/^#PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
RUN rm /etc/ssh/ssh_host_*  
  
EXPOSE 22  
# Add test data owner  
RUN useradd -d /home/${USER} -g users -u 1000 -m -s /bin/bash ${USER}  
  
RUN echo "${USER}"':passwordpassword' |chpasswd  
  
# Prepare bench test directory and change owner  
RUN mkdir -p /export/sshfs && \  
mkdir -p /export/xrosfs && \  
chown ${USER} /export && \  
chown ${USER} /export/sshfs && \  
chown ${USER} /export/xrosfs  
  
# Prepare bench test data  
USER ${USER}  
  
RUN echo 'hello sshfs' > /export/sshfs/hello.txt && \  
echo 'hello xrosfs' > /export/xrosfs/hello.txt  
  
COPY setup-scripts/setup-bench-basic-data.sh /tmp/  
RUN sh /tmp/setup-bench-basic-data.sh  
  
COPY setup-scripts/setup-bench-useruri-data.sh /tmp/  
RUN sh /tmp/setup-bench-useruri-data.sh  
  
USER root  
  
COPY setup-scripts/setup-bench-relpath-data.sh /tmp/  
RUN sh /tmp/setup-bench-relpath-data.sh  
  
COPY start.sh /tmp/start.sh  
  
CMD ["sh", "/tmp/start.sh"]  

