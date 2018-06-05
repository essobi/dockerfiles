FROM centos:latest  
MAINTAINER cmsj@tenshu.net  
RUN yum install -y deltarpm yum-utils && \  
yum update -y && \  
yum install avahi -y && \  
yum clean all  
RUN mkdir -p /var/run/dbus  
RUN sed -i -e 's/#host-name=foo/host-name=nucker/' /etc/avahi/avahi-
daemon.conf  
RUN sed -i -e 's/avahi-daemon -s/avahi-daemon -s --no-drop-root/'
/usr/lib/systemd/system/avahi-daemon.service  
VOLUME /var/run/dbus  
ENTRYPOINT avahi-daemon --no-drop-root  
LABEL INSTALL /usr/bin/docker run --privileged --rm --volume /:/host --name
NAME IMAGE cp -v /etc/dbus-1/system.d/avahi-dbus.conf
/host/etc/dbus-1/system.d/  
LABEL UNINSTALL /usr/bin/docker run --privileged --rm --volume /:/host -name
NAME IMAGE rm /host/etc/dbus-1/system.d/avahi-dbus.conf  

