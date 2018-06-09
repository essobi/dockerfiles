FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y \  
openssh-server \  
vim \  
python \  
parted \  
gdisk \  
cgpt \  
iproute \  
kexec-tools \  
jq \  
rsync \  
dstat \  
fio \  
lshw \  
iperf3 \  
sshpass \  
ansible \  
libaio1 \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /var/run/sshd  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
RUN mkdir -m 700 /root/.ssh  
RUN mkdir -p /opt  
ADD bin /opt/bin  
ENV PATH /opt/bin:$PATH  
ADD README.md /README.md  
  
RUN rm -f /etc/ssh/sshd_config  
ADD sshd_config /etc/ssh/sshd_config  
  
RUN echo "alias docker='LD_LIBRARY_PATH=$(dirname $(find $(readlink -f /lib)
-iname libdl.so.2)):/host/lib docker'" >> /root/.bashrc  
  
# Regenerating host key of sshd  
RUN rm -rf /etc/ssh/ssh_host*  
RUN ssh-keygen -q -f /etc/ssh/ssh_host_dsa_key -N '' -t dsa  
RUN ssh-keygen -q -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa  
RUN ssh-keygen -q -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa  
RUN ssh-keygen -q -f /etc/ssh/ssh_host_ed25519_key -N '' -t ed25519  
  
VOLUME ["/root"]  
  
EXPOSE 2222  
CMD ["/usr/sbin/sshd", "-D"]  

