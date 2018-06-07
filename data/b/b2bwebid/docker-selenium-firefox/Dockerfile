FROM ryht/debian:jessie  
LABEL authors="B2B Data Analist"  
  
#================================================  
# Customize sources for apt-get  
#================================================  
RUN echo "deb http://deb.debian.org/debian jessie main contrib non-free\n" >
/etc/apt/sources.list \  
&& echo "deb http://deb.debian.org/debian jessie-updates main contrib non-
free\n" >> /etc/apt/sources.list \  
&& echo "deb http://security.debian.org/ jessie/updates main contrib non-
free\n" >> /etc/apt/sources.list \  
&& echo "deb http://ftp.debian.org/debian jessie-backports main\n" >>
/etc/apt/sources.list  
  
# No interactive frontend during docker build  
ENV DEBIAN_FRONTEND=noninteractive \  
DEBCONF_NONINTERACTIVE_SEEN=true  
  
#========================  
# Miscellaneous packages  
# Includes minimal runtime used for executing non GUI Java programs  
#========================  
RUN apt-get -y update \  
&& apt-get -y install \  
bzip2 \  
ca-certificates \  
tzdata \  
sudo \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
RUN apt-get -y update \  
&& apt-get -y install \  
openjdk-7-jre-headless \  
&& sed -i
's/securerandom\\.source=file:\/dev\/random/securerandom\\.source=file:\/dev\/urandom/'
\  
./usr/lib/jvm/java-7-openjdk-amd64/jre/lib/security/java.security  
  
#===================  
# Timezone settings  
# Possible alternative:
https://github.com/docker/docker/issues/3359#issuecomment-32150214  
#===================  
ENV TZ "UTC"  
RUN echo "${TZ}" > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
#========================================  
# Add normal user with passwordless sudo  
#========================================  
RUN useradd seluser \  
\--shell /bin/bash \  
\--create-home \  
&& usermod -a -G sudo seluser \  
&& echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \  
&& echo 'seluser:secret' | chpasswd  
  
#===================================================  
# Run the following commands as non-privileged user  
#===================================================  
USER seluser  
  
#==========  
# Selenium  
#==========  
RUN sudo mkdir -p /opt/selenium \  
&& sudo chown seluser:seluser /opt/selenium \  
&& wget --no-verbose https://selenium-
release.storage.googleapis.com/3.4/selenium-server-standalone-3.4.0.jar \  
-O /opt/selenium/selenium-server-standalone.jar  
  
#==============  
# Node Base  
#==============  
USER root  
  
#==============  
# VNC and Xvfb  
#==============  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
locales \  
xvfb \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
#==============  
# Install driver  
#==============  
USER root  
  
#=========  
# Firefox  
#=========  
ARG FIREFOX_VERSION=54.0.1  
RUN wget --no-verbose -O /tmp/firefox.tar.bz2 https://download-
installer.cdn.mozilla.net/pub/firefox/releases/$FIREFOX_VERSION/linux-x86_64/en-
US/firefox-$FIREFOX_VERSION.tar.bz2 \  
&& rm -rf /opt/firefox \  
&& tar -C /opt -xjf /tmp/firefox.tar.bz2 \  
&& rm /tmp/firefox.tar.bz2 \  
&& ln -fs /opt/firefox/firefox /usr/bin/firefox  
  
#============  
# GeckoDriver  
#============  
ARG GECKODRIVER_VERSION=0.17.0  
RUN wget --no-verbose -O /tmp/geckodriver.tar.gz
https://github.com/mozilla/geckodriver/releases/download/v$GECKODRIVER_VERSION/geckodriver-v$GECKODRIVER_VERSION-
linux64.tar.gz \  
&& mkdir -p /opt/geckodriver \  
&& tar -C /opt/geckodriver -zxf /tmp/geckodriver.tar.gz \  
&& rm /tmp/geckodriver.tar.gz \  
&& chmod 755 /opt/geckodriver/geckodriver \  
&& ln -fs /opt/geckodriver/geckodriver /usr/bin/geckodriver  
  
USER seluser  
  
COPY generate_config /opt/bin/generate_config  
  
# Running this command as sudo just to avoid the message:  
# To run a command as administrator (user "root"), use "sudo <command>". See
"man sudo_root" for details.  
# When logging into the container  
RUN sudo echo ""  
  
#====================================  
# Scripts to run Selenium Standalone  
#====================================  
COPY entry_point.sh /opt/bin/entry_point.sh  
  
EXPOSE 4444  
CMD ["/opt/bin/entry_point.sh"]  

