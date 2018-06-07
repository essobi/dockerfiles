##Download base image ubuntu Centos 7  
FROM centos:7  
MAINTAINER Lorenzo Comotti  
  
##Define the ENV variable  
ENV TERRARIA_VERSION=1.3.5.3  
ENV TERRARIA_CONF /opt/terraria/Linux/  
  
##Update Software repository  
RUN yum -y update  
  
##Install required pakages  
RUN yum -y install wget && yum -y install unzip && yum -y install screen  
  
##Download Terraria Server  
RUN cd /opt && curl -O http://terraria.org/server/terraria-server-1353.zip  
  
##Extract the archive  
RUN mkdir -p /opt/terraria && unzip -o /opt/terraria-server-1353.zip -d
/opt/terraria && mv -vn /opt/terraria/1353/* /opt/terraria/ && rm -R -f
/opt/1353  
  
##Set permission  
RUN chown -R root:root /opt/terraria && chmod +x
/opt/terraria/Linux/TerrariaServer.bin.x86_64  
  
##Create user  
RUN id -u terraria &>/dev/null || useradd -r -m -d /srv/terraria terraria  
  
##Remove ZIP file  
RUN rm /opt/terraria-server-1353.zip  
  
##Copy coinfiguration File  
COPY serverconfig.txt ${TERRARIA_CONF}  
COPY server-start.sh ${TERRARIA_CONF}  
  
RUN chmod +x ${TERRARIA_CONF}server-start.sh  
  
##Volume configuration  
VOLUME [ "/var/terraria-worlds/" ]  
  
WORKDIR "/opt/terraria/Linux"  
  
ENTRYPOINT [ "/bin/bash" ]  
  
EXPOSE 7777  

