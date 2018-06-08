FROM ubuntu:utopic  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Update apt sources contents  
RUN sed 's/main$/main universe/' -i /etc/apt/sources.list && apt-get update  
  
#Set fr_FR.UTF-8 as default locale  
RUN locale-gen fr_FR.UTF-8 && dpkg-reconfigure locales  
ENV LANGUAGE fr_FR.UTF-8  
ENV LANG fr_FR.UTF-8  
ENV LC_ALL fr_FR.UTF-8  
# Prepare for OpenJDK 7  
# Fake a fuse install -- required for openjdk-7  
# from https://gist.github.com/henrik-muehe/6155333  
RUN apt-get update && apt-get install libfuse2 && apt-get clean  
RUN cd /tmp && mkdir fuseinst && cd fuseinst && apt-get download fuse && dpkg-
deb -x fuse_* . && dpkg-deb -e fuse_* && rm fuse_*.deb && /bin/echo -en
'#!/bin/bash\nexit 0\n' > DEBIAN/postinst && dpkg-deb -b . /fuse.deb && dpkg
-i /fuse.deb && rm -rf /tmp/fuseinst && cd /  
  
# Proceed with installations  
RUN apt-get update && apt-get install -y apt-transport-https openjdk-7-jdk
curl wget supervisor unzip rsync git ssh python-software-properties software-
properties-common libaio1 && apt-get clean  
  
# Run supervisord by default  
CMD ["/usr/bin/supervisord", "--nodaemon", "--
configuration=/etc/supervisor/supervisord.conf"]  

