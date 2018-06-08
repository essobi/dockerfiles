FROM ubuntu:17.10  
  
# Install X11 support  
RUN echo "Install X11 support" && \  
apt-get update && \  
apt-get install -y xorg openbox && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo "Install Oracle Java 1.8" && \  
apt-get update && \  
apt-get install -y software-properties-common python-software-properties && \  
add-apt-repository ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y debconf-utils && \  
echo "Installing Java..." && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select true"
| debconf-set-selections && \  
echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 seen true" |
debconf-set-selections && \  
apt-get install -y oracle-java8-installer && \  
echo "Removing installed packages" && \  
apt-get remove -y software-properties-common python-software-properties
debconf-utils oracle-java8-installer && \  
echo "Cleaning apt-get fetched temporal files" && \  
rm -rf /var/lib/apt/lists/*  
  
# Line to install Oxygen  
#RUN wget
http://eclipse.c3sl.ufpr.br/technology/epp/downloads/release/oxygen/1a/eclipse-
jee-oxygen-1a-linux-gtk-x86_64.tar.gz -O ~/eclipse.tar.gz  
  
RUN echo "Install Eclipse STS based on Oxygen (4.7.1a)" && \  
apt-get install -y \--no-install-recommends wget && \  
wget
http://download.springsource.com/release/STS/3.9.1.RELEASE/dist/e4.7/spring-
tool-suite-3.9.1.RELEASE-e4.7.1a-linux-gtk-x86_64.tar.gz -O ~/eclipse.tar.gz
&& \  
tar zxvf ~/eclipse.tar.gz && \  
rm ~/eclipse.tar.gz && \  
apt-get remove -y wget && \  
rm -rf /var/lib/apt/lists/*  
  
  
# Adjust eclipse configuration  
#RUN echo "Adjust Eclipse configuration" && \  
#echo "#!/bin/sh" > adjustEclipseConfig.sh  
#RUN echo "awk '" >> adjustEclipseConfig.sh  
  
# Configure volumes for repository and workspace  
VOLUME /root/repo  
VOLUME /root/eclipse-workspace  
  
  
  
# Launch eclipse  
CMD /sts-bundle/sts-3.9.1.RELEASE/STS

