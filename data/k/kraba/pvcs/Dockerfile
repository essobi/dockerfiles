FROM ubuntu:latest  
MAINTAINER Matteo Basso matteo.basso@gmail.com  
  
ENV LOGNAME root  
  
#Add dmsys user/group/home  
RUN groupadd dmtool && \  
useradd -d /home/dmsys -m -Gdmtool dmsys  
  
# Change UID and GID of dmsys/dmtool user to match host privileges  
ARG DMSYS_USER_UID=999  
ARG DMSYS_USER_GID=999  
ARG DMSYS_PASSWD=dmsys  
RUN usermod -u $DMSYS_USER_UID dmsys && \  
groupmod -g $DMSYS_USER_GID dmtool && \  
echo "dmsys:$DMSYS_PASSWD" | chpasswd  
  
#Add PVCS user/group/home  
RUN groupadd pvcs && \  
useradd -d /data -m -gpvcs pvcs  
  
# Change UID and GID of pvcs/pvcs user to match host privileges  
ARG PVCS_USER_UID=998  
ARG PVCS_USER_GID=998  
ARG PVCS_PASSWD=remedy  
RUN usermod -u $PVCS_USER_UID pvcs && \  
groupmod -g $PVCS_USER_GID pvcs && \  
echo "pvcs:$PVCS_PASSWD" | chpasswd  
  
#Package required by Serena/Remedy/PVCS Dimension  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y bc libocamlnet-ocaml-dev libsasl2-2 libc6:i386
libncurses5:i386 libstdc++6:i386 net-tools iproute2 --no-install-recommends  
  
#Serena/Remedy/PVCS Dimension "installation"  
##############################################  
#PLEASE UNCOMMENT AND SELECT YOUR FILE SOURCE#  
##############################################  
#ARG SERENA_FILE=serena.tar.gz  
#COPY file/$SERENA_FILE /opt  
#RUN tar -zxf /opt/$SERENA_FILE -C /opt && \  
# echo "pcms_sdp 1055/tcp" >> /etc/services  
  
# Supervisord conf  
RUN apt-get install -y supervisor --no-install-recommends  
RUN mkdir -p /var/log/supervisor  
COPY script/supervisord.conf /etc/supervisor/conf.d/  
  
#Script for remedy --> supervisor  
COPY script/remedyalive.sh /home/dmsys/  
RUN chmod 500 /home/dmsys/remedyalive.sh  
  
# SSH Server setup  
RUN apt-get install -y openssh-server --no-install-recommends && \  
mkdir -p /var/run/sshd; \  
chmod 700 /var/run/sshd; \  
echo "AllowUsers pvcs" >> /etc/ssh/sshd_config; \  
mkdir -p /data/.ssh; \  
chmod 700 /data/.ssh; \  
ssh-keygen -q -t rsa -b 2048 -f /data/.ssh/id_dsa -N '' -C 'PVCS keypair
generated during docker build' && cat /data/.ssh/id_dsa.pub >
/data/.ssh/authorized_keys; \  
chmod 600 /data/.ssh/authorized_keys;  
  
#Useful package for working area  
RUN apt-get install -y zip unzip vim --no-install-recommends  
  
#Removing apt lists  
RUN rm -r /var/lib/apt/lists/*  
  
VOLUME ["/data"]  
WORKDIR /data  
EXPOSE 22 1055  
CMD ["/usr/bin/supervisord", "-n"]

