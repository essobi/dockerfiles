FROM ubuntu:trusty  
  
MAINTAINER Mikael Kalms <mikael@kalms.org>  
  
RUN apt-get update  
RUN apt-get install -y wget apt-transport-https openssh-client  
  
RUN mkdir /conf  
RUN mkdir /logs  
RUN mkdir -p /db/sqlite  
  
RUN echo "deb http://www.plasticscm.com/plasticrepo/plasticscm-
common/Ubuntu_14.04/ ./" > /etc/apt/sources.list.d/plastic.list  
RUN echo "deb http://www.plasticscm.com/plasticrepo/plasticscm-
latest/Ubuntu_14.04/ ./" >> /etc/apt/sources.list.d/plastic.list  
RUN wget -q http://www.plasticscm.com/plasticrepo/plasticscm-
common/Ubuntu_14.04/Release.key -O - | apt-key add -  
RUN wget -q http://www.plasticscm.com/plasticrepo/plasticscm-
latest/Ubuntu_14.04/Release.key -O - | apt-key add -  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -q update && apt-get install -y -q
plasticscm-complete && plasticsd stop  
  
RUN mkdir /root/.ssh  
  
RUN { \  
clconfigureserver --language=en --port=8087 --workingmode=UPWorkingMode; \  
[ -f /opt/plasticscm5/server/users.conf ] && mv
/opt/plasticscm5/server/users.conf /conf || touch /conf/users.conf; \  
[ -f /opt/plasticscm5/server/groups.conf ] && mv
/opt/plasticscm5/server/groups.conf /conf || touch /conf/groups.conf; \  
mv /opt/plasticscm5/server/plasticd.lic /conf; \  
ln -s /conf/users.conf /opt/plasticscm5/server && ln -s /conf/groups.conf
/opt/plasticscm5/server; \  
ln -s /conf/plasticd.lic /opt/plasticscm5/server; \  
ln -s /conf/plasticd.token.lic /opt/plasticscm5/server; \  
ln -s /conf/client.conf /opt/plasticscm5/client/client.conf; \  
ln -s /conf/cryptedservers.conf /opt/plasticscm5/server/cryptedservers.conf; \  
ln -s /conf/id_rsa /root/.ssh/id_rsa; \  
ln -s /conf/ssh_config /root/.ssh/config; \  
ln -s /conf/known_hosts /root/.ssh/known_hosts; \  
ln -s /conf/replication /etc/init.d/replication; \  
}  
  
RUN umtool cu root root  
RUN umtool cg administrators  
RUN umtool autg root administrators  
  
ADD loader.log.conf /opt/plasticscm5/server/  
ADD db.conf /opt/plasticscm5/server/  
ADD client.conf /conf/  
ADD ssh_config /conf/  
ADD replication /conf/  
  
RUN chmod 755 /etc/init.d/replication /conf/replication  
  
VOLUME /conf  
VOLUME /db/sqlite  
VOLUME /logs  
  
ADD *.sh /root/  
RUN chmod u+x /root/*.sh  
CMD ["sh", "/root/start.sh"]  

