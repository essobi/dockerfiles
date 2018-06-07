FROM newtork/groupware-domain-stub:latest  
  
MAINTAINER newtork / Alexander Dümont <alexander_duemont@web.de>  
  
  
##########################################  
# #  
# Docker Build #  
# #  
##########################################  
  
# TODO add ENV vars to BASH INPUTS  
#  
# USAGE  
# -----  
# docker pull newtork/groupware-domain  
# docker build -t newtork/groupware-domain .  
#  
# See README for run command.  
#  
  
##########################################  
# #  
# Arguments #  
# #  
##########################################  
  
ARG AD_PATH  
ENV AD_PATH ${AD_PATH:-/data/ad01}  
  
ARG AD_NAME  
ENV AD_NAME ${AD_NAME:-MY}  
  
ARG AD_ADMIN  
ENV AD_ADMIN ${AD_ADMIN:-Administrator}  
  
ARG AD_FQN  
ENV AD_FQN ${AD_FQN:-MY.EXAMPLE.COM}  
  
ARG AD_PASSWORD  
ENV AD_PASSWORD ${AD_PASSWORD:-Passw0rd}  
  
ARG INTERFACE  
ENV INTERFACE ${INTERFACE:-eth0}  
  
ARG IP_SELF  
ENV IP_SELF ${IP_SELF:-127.0.0.1}  
  
ARG IP_PEER  
ENV IP_PEER ${IP_PEER:-""}  
  
ARG LOCAL_DIR_SELF  
ENV LOCAL_DIR_SELF ${LOCAL_DIR_SELF:-/root/dc/}  
  
ARG LOCAL_DIR_PEER  
ENV LOCAL_DIR_PEER ${LOCAL_DIR_PEER:-$LOCAL_DIR_SELF}  
  
ARG HOSTNAME_PEER  
ENV HOSTNAME_PEER ${HOSTNAME_PEER:-""}  
  
ARG SYNC_USER_PEER  
ENV SYNC_USER_PEER ${SYNC_USER_PEER:-root}  
  
ARG SYNC_USER_SELF  
ENV SYNC_USER_SELF ${SYNC_USER_SELF:-root}  
  
ARG SYNC_SSH_SELF  
ENV SYNC_SSH_SELF ${SYNC_SSH_SELF:-/root/.ssh/}  
  
ARG SYNC_PORT_SELF  
ENV SYNC_PORT_SELF ${SYNC_PORT_SELF:-22137}  
  
ARG SYNC_PORT_PEER  
ENV SYNC_PORT_PEER ${SYNC_PORT_PEER:-$SYNC_PORT_SELF}  
  
ARG SYNC_DIR_SELF  
ENV SYNC_DIR_SELF ${SYNC_DIR_SELF:-""}  
  
ARG OSYNC_VERSION  
ENV OSYNC_VERSION ${OSYNC_VERSION:-1.1.3}  
ENV SYNC_EXEC "${LOCAL_DIR_SELF}/osync-${OSYNC_VERSION}/osync-srv start"  
  
  
##########################################  
# #  
# Build Settings / Environment #  
# #  
##########################################  
  
#### Port Usage for samba active directory  
#  
# Service Port Protocol  
# -------------------- -------- --------  
# DNS 53 tcp/udp  
# Kerberos 88 tcp/udp  
# End Point Mapper 135 tcp  
# NetBIOS Name Service 137 udp  
# NetBIOS Datagram 138 udp  
# NetBIOS Session 139 tcp  
# LDAP 389 tcp/udp  
# SMB over TCP 445 tcp  
# Kerberos kpasswd 464 tcp/udp  
# LDAPS 636 tcp  
# Dynamic RPC Ports 1024-5000 tcp  
# Global Cataloge 3268 tcp  
# Global Cataloge SSL 3269 tcp  
  
EXPOSE 53 88 135 137 138 139 389 445 464 636 1024-1152 3268 3269  
  
  
# Service Port Protocol  
# -------------------- -------- --------  
# Sysvol Replication 22137 tcp  
  
EXPOSE $SYNC_PORT_SELF  
  
  
  
# just start in root  
WORKDIR $LOCAL_DIR_SELF  
  
  
  
##########################################  
# #  
# PREPARATION #  
# #  
##########################################  
  
  
ARG RUNTIME_PACKAGES="rsync openssh-client openssh-server inotify-tools ldb-
tools"  
ARG BUILD_PACKAGES="wget"  
  
#  
# Build-Process:  
# --------------  
#  
# 1) Just download and install required packages.  
#  
#  
  
RUN apt-get -qq update && \  
apt-get -yqq install ${RUNTIME_PACKAGES} ${BUILD_PACKAGES} && \  
  
sed -i "s/^Port 22$/Port ${SYNC_PORT_SELF}/" /etc/ssh/sshd_config && \  
sed -i -r "s/#?PasswordAuthentication (yes|no)/PasswordAuthentication no/"
/etc/ssh/sshd_config && \  
sed -i -r "s/#?PermitRootLogin (yes|no|without-password)/PermitRootLogin
without-password/" /etc/ssh/sshd_config && \  
  
wget "https://github.com/deajan/osync/archive/v${OSYNC_VERSION}.tar.gz" && \  
tar -xzf v${OSYNC_VERSION}.tar.gz && rm v${OSYNC_VERSION}.tar.gz && \  
cd osync-${OSYNC_VERSION} && echo "n" | ./install.sh && \  
  
apt-get remove --purge -y ${BUILD_PACKAGES} && \  
rm -rf /var/lib/apt/lists/* && \  
echo "Cleared temporary data."  
  
  
  
  
ENV DC_SH_ALIAS="docker run groupware-domain"  
COPY scripts/*.sh ${LOCAL_DIR_SELF}  
COPY sync.conf /etc/osync/sync.conf.tmp  
  
RUN chmod +x ${LOCAL_DIR_SELF}/dc*.sh  
  
###############################################  
# #  
# START #  
# #  
###############################################  
  
# Use the server wrapper file, no default CMD / arguments  
ENTRYPOINT ["/root/dc/dc.sh"]  
  

