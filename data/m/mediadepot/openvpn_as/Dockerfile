FROM debian:jessie  
MAINTAINER jason@thesparktree.com  
  
#Create internal depot user (which will be mapped to external DEPOT_USER, with
the uid and gid values)  
RUN groupadd -g 15000 -r depot && useradd --uid 15000 -r -g depot depot  
  
#TODO: determine if we need to setup user account for openvpn_as to login
with.  
#Install base applications + deps  
RUN echo "deb http://http.us.debian.org/debian stable main contrib non-free" |
tee -a /etc/apt/sources.list  
RUN apt-get -q update && \  
apt-get install -qy --force-yes git-core iptables curl && \  
apt-get -y autoremove && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
#Create confd folder structure  
RUN curl -L -o /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v0.11.0/confd-
linux-amd64  
RUN chmod u+x /usr/local/bin/confd  
ADD ./conf.d /etc/confd/conf.d  
ADD ./templates /etc/confd/templates  
  
#Create OpenVPN AS folder structure & set as volumes  
RUN mkdir -p /srv/openvpn/data  
  
#Install OpenVPN  
RUN curl -L http://swupdate.openvpn.org/as/openvpn-
as-2.0.21-Ubuntu14.amd_64.deb -o openvpn-as-2.0.21-Ubuntu14.amd_64.deb && \  
dpkg -i openvpn-as-2.0.21-Ubuntu14.amd_64.deb && \  
rm /openvpn-as-2.0.21-Ubuntu14.amd_64.deb && \  
rm -f /usr/local/openvpn_as/etc/as.conf  
  
#Copy over start script and docker-gen files  
ADD ./start.sh /srv/start.sh  
RUN chmod u+x /srv/start.sh  
  
VOLUME ["/srv/openvpn/data"]  
  
EXPOSE 943  
#TCP Port  
EXPOSE 60000  
#UDP Port  
EXPOSE 60001  
CMD ["/srv/start.sh"]  

