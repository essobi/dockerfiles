###############################################################################  
# Jitterbit Data Loader Agent  
# Made at (bandit.io)  
###############################################################################  
FROM phusion/baseimage:0.9.19  
  
###############################################################################  
ENV INSTALL_DIR=/opt/install \  
INSTALL_FILE=jibberbit.deb \  
JITTERBIT_HOME=/opt/jitterbit  
  
#
https://success.jitterbit.com/display/DOC/Download+and+Install+Harmony+Linux+Agent  
RUN dpkg --add-architecture i386 && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
libc6:i386 \  
libgcc1:i386 \  
libstdc++6:i386 \  
libuuid1:i386 \  
zlib1g:i386 && \  
apt-get install -y --no-install-recommends \  
unixodbc \  
python \  
sed \  
sudo \  
unzip \  
tar  
  
COPY scripts/startup/*.sh /etc/my_init.d/  
  
RUN chmod +x /etc/my_init.d/*.sh && \  
groupadd -g 1000 jitterbit && \  
useradd -u 1000 -g jitterbit -m jitterbit && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV V_MAJOR=8 \  
V_MINOR=23 \  
V_PATCH=0 \  
V_BUILD=10  
  
ENV
JITTERBIT_LINK=https://download.jitterbit.com/v${V_MAJOR}/agent/${V_MAJOR}.${V_MINOR}/jitterbit-
agent_${V_MAJOR}.${V_MINOR}.${V_PATCH}.${V_BUILD}_i386.deb  
  
ADD ${JITTERBIT_LINK} ${INSTALL_DIR}/${INSTALL_FILE}  
  
EXPOSE 46914  
  
CMD ["/sbin/my_init"]

