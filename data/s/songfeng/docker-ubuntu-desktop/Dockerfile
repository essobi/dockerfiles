FROM ubuntu:16.04  
LABEL description="ubuntu docker with xfce desktop"  
LABEL version="1.0"  
LABEL maintainer="Feng Song <franksongfeng@yahoo.com>"  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y \  
apt-utils net-tools iputils-ping ufw lsof curl netcat wget bzip2 vim-tiny \  
supervisor \  
openssh-server \  
xfce4 xfce4-goodies \  
x11vnc xvfb \  
firefox  
RUN apt-get install -y \  
python python-pip python3 python3-pip \  
erlang erlang-xmlrpc erlang-lager erlang-jiffy rebar  
COPY requirements.txt /etc/requirements.txt  
RUN pip install -r /etc/requirements.txt  
RUN apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
ARG ROOT_PWD=admin  
ARG PORT_VNC=5900  
ARG PORT_SSH=22  
RUN mkdir -p /var/run/sshd && \  
echo 'root:'${ROOT_PWD} | chpasswd && \  
sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config &&
\  
sed -ri "s/^Port\s+.*/Port ${PORT_SSH}/" /etc/ssh/sshd_config && \  
sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
EXPOSE \  
${PORT_VNC} \  
${PORT_SSH}  
  
WORKDIR /root  
COPY startup.sh ./  
COPY supervisord.conf ./  
ENTRYPOINT ["./startup.sh"]  

