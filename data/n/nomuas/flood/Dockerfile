FROM centos  
  
LABEL maintainer="Frederic S." mail="nomuas@gmail.com"  
LABEL description="Minimum install for flood"  
LABEL git="https://github.com/jfurrow/flood"  
LABEL version="1.0"  
  
# User environment  
ENV USERNAME=flood \  
USERID=911 \  
GROUPID=911  
# App environment  
ENV NODE_VERSION=9 \  
FLOOD_VERSION=v1.0.0  
# git clone https://github.com/jfurrow/flood  
# Install NodeJS, clean yum and add user  
RUN curl -sL https://rpm.nodesource.com/setup_${NODE_VERSION}.x | bash - && \  
yum -y update && \  
yum -y upgrade && \  
yum -y install nodejs && \  
yum -y autoremove && \  
yum -y clean all && \  
rm -rf /var/lib/yum/yum.db/* /tmp/* /var/tmp/* && \  
groupadd -g ${GROUPID} ${USERNAME} && \  
useradd -u ${USERID} -g ${GROUPID} -m -d /home/${USERNAME} -s /sbin/nologin
${USERNAME} && \  
cd /home/${USERNAME} && \  
curl -sL -o - https://github.com/jfurrow/flood/archive/${FLOOD_VERSION}.tar.gz
| tar xzvf - --strip-components=1 && \  
npm install --production && \  
mkdir /config /run/rtorrent /downloads && \  
chown -R ${USERNAME}:${USERNAME} /home/${USERNAME} /config /run/rtorrent
/downloads  
  
COPY root/ /  
  
VOLUME /config /run/rtorrent  
  
EXPOSE 3000  
USER ${USERNAME}  
  
WORKDIR /home/${USERNAME}  
  
CMD ["init_flood.sh"]  

