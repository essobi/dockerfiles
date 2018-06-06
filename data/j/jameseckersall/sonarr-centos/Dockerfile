FROM centos:7  
MAINTAINER James Eckersall <james.eckersall@gmail.com>  
  
RUN \  
yum install -y epel-release yum-utils && \  
rpm --import
"http://keyserver.ubuntu.com/pks/lookup?op=get&search=0x3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF"
&& \  
yum-config-manager --add-repo http://download.mono-project.com/repo/centos/ &&
\  
yum install -y wget mediainfo libzen libmediainfo curl gettext mono-core mono-
devel sqlite.x86_64 && \  
yum clean all && \  
mkdir --mode=0777 /config  
  
RUN \  
curl -L http://update.sonarr.tv/v2/master/mono/NzbDrone.master.tar.gz -o
/tmp/NzbDrone.master.tar.gz && \  
tar -xvf /tmp/NzbDrone.master.tar.gz -C / && \  
rm -f NzbDrone.master.tar.gz && \  
rm -rf /var/cache/yum/* >/dev/null 2>&1 || true && \  
chmod -R 0777 /var/log /run /config /NzbDrone  
  
# Needed for signalr to work (see https://forums.sonarr.tv/t/gui-update-
issues/4195/31)  
ENV XDG_CONFIG_HOME=/config  
  
EXPOSE 8989  
VOLUME ["/config", "/data"]  
  
ENTRYPOINT [ "/usr/bin/mono", "/NzbDrone/NzbDrone.exe", "-nobrowser",
"-data=/config" ]  

