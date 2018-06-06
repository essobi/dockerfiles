FROM convox/rails  
  
MAINTAINER Ryan Caught "rcaught@gmail.com"  
RUN apt-get update -qq && apt-get install -y -qq git locales curl  
  
RUN locale-gen en_US.UTF-8  
  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8  
RUN apt-get install -y -qq \  
xvfb \  
qt5-default \  
libqt5webkit5-dev \  
qt5-qmake \  
gstreamer1.0-plugins-base \  
gstreamer1.0-tools \  
gstreamer1.0-x  
  
RUN curl -Ls https://install.convox.com/linux.zip > /tmp/convox.zip \  
&& unzip /tmp/convox.zip -d /usr/local/bin  

