FROM ubuntu:16.04  
MAINTAINER Selenium <selenium-developers@googlegroups.com>  
  
USER root  
  
#================================================  
# Customize sources for apt-get  
#================================================  
RUN echo "deb http://archive.ubuntu.com/ubuntu xenial main universe\n" >
/etc/apt/sources.list \  
&& echo "deb http://archive.ubuntu.com/ubuntu xenial-updates main universe\n"
>> /etc/apt/sources.list \  
&& echo "deb http://security.ubuntu.com/ubuntu xenial-security main
universe\n" >> /etc/apt/sources.list  
  
#========================  
# Miscellaneous packages  
# Includes minimal runtime used for executing non GUI Java programs  
#========================  
RUN apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
bzip2 \  
tzdata \  
ca-certificates \  
openjdk-8-jre-headless \  
sudo \  
unzip \  
wget \  
&& rm -rf /var/lib/apt/lists/* \  
&& sed -i
's/securerandom\\.source=file:\/dev\/random/securerandom\\.source=file:\/dev\/urandom/'
./usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.security  
  
#==========  
# Selenium  
#==========  
RUN apt-get update  
RUN mkdir -p /opt/selenium  
ADD selenium-server-standalone-2.49.1.jar /opt/selenium/selenium-server-
standalone.jar  
  
RUN apt-get install gconf-service libasound2 libatk1.0-0 libc6 libcairo2
libcups2 libdbus-1-3 libexpat1 libfontconfig1 libfreetype6 libgcc1
libgconf-2-4 libgdk-pixbuf2.0-0 libglib2.0-0 libgtk2.0-0 libnspr4 libnss3
libpango1.0-0 libstdc++6 libx11-6 libxcomposite1 libxcursor1 libxdamage1
libxext6 libxfixes3 libxi6 libxrandr2 libxrender1 libxss1 libxtst6 ca-
certificates fonts-liberation libappindicator1 libcurl3 lsb-base xdg-utils
wget -y  
ADD google-chrome-stable_52.0.2743.116_amd64.deb /google-chrome-
stable_52.0.2743.116_amd64.deb  
RUN dpkg -i /google-chrome-stable_52.0.2743.116_amd64.deb  
RUN apt-get -f install -y  
  
COPY chrome_launcher.sh /opt/google/chrome/google-chrome  
RUN chmod +x /opt/google/chrome/google-chrome  
  
# Chrome Driver  
ADD chromedriver_linux64-2.21.zip /chromedriver_linux64-2.21.zip  
RUN unzip /chromedriver_linux64-2.21.zip  
RUN chmod 0775 /chromedriver  
  
#========================================  
# Add normal user with passwordless sudo  
#========================================  
RUN sudo useradd seluser --shell /bin/bash --create-home \  
&& sudo usermod -a -G sudo seluser \  
&& echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \  
&& echo 'seluser:secret' | chpasswd  
  
EXPOSE 4444  
ENV DEBIAN_FRONTEND noninteractive  
ENV DEBCONF_NONINTERACTIVE_SEEN true  
  
#===================  
# Timezone settings  
# Possible alternative:
https://github.com/docker/docker/issues/3359#issuecomment-32150214  
#===================  
ENV TZ "US/Pacific"  
RUN echo "${TZ}" > /etc/timezone \  
&& dpkg-reconfigure --frontend noninteractive tzdata  
  
#==============  
# VNC and Xvfb  
#==============  
RUN apt-get update -qqy \  
&& apt-get -qqy install \  
xvfb \  
x11vnc \  
net-tools \  
&& rm -rf /var/lib/apt/lists/*  
  
#==============================  
# Scripts to run Selenium Node  
#==============================  
RUN mkdir -p /opt/bin  
  
COPY \  
entry_point.sh \  
functions.sh \  
/opt/bin/  
RUN chmod +x /opt/bin/entry_point.sh  
  
#============================  
# Some configuration options  
#============================  
# Set wide enough to accomodate 1500x800 and lower  
ENV SCREEN_WIDTH 1600  
ENV SCREEN_HEIGHT 1020  
ENV SCREEN_DEPTH 24  
ENV DISPLAY :99.0  
USER seluser  
  
CMD ["/opt/bin/entry_point.sh"]  
  

