FROM centos:centos7  
  
ENV DISPLAY :99.0  
ENV FF_VERSION 40.0  
ENV RUBY_VERSION 2.2  
RUN yum install -y centos-release-scl && yum clean all -y  
RUN yum install -y epel-release && yum clean all -y  
RUN yum install -y --setopt=tsflags=nodocs \  
make git bzip2 fontconfig libXrender.x86_64 libXcomposite.x86_64 sqlite
sqlite-devel \  
gtk2.x86_64 alsa-utils alsa-lib xorg-x11-server-Xvfb dbus-glib \  
dejavu-sans-fonts dejavu-serif-fonts rh-ruby22 rh-ruby22-ruby-devel \  
rh-ruby22-rubygem-rake v8314 rh-ruby22-rubygem-bundler nodejs010 mysql-devel
wget \  
x11vnc && \  
yum clean all -y  
  
RUN wget "https://download-
installer.cdn.mozilla.net/pub/firefox/releases/${FF_VERSION}/linux-x86_64/en-
US/firefox-${FF_VERSION}.tar.bz2" \  
-O /tmp/firefox.tar.bz2 && \  
tar xvf /tmp/firefox.tar.bz2 -C /usr/local && \  
ln -s /usr/local/firefox/firefox /usr/bin/firefox && \  
rm /tmp/firefox.tar.bz2  
  
RUN dbus-uuidgen > /etc/machine-id  
  
ADD enableruby22.sh /etc/profile.d/enableruby22.sh  
ADD localbin.sh /etc/profile.d/localbin.sh  
RUN chmod 755 /etc/profile.d/*.sh  
  
RUN mkdir -p /opt/src  
VOLUME /opt/src  
  
ADD bin/cucumber-entry /usr/bin/cucumber-entry  
  
WORKDIR /opt/src  
  
CMD /usr/bin/cucumber-entry  

