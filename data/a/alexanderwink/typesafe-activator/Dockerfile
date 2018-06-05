FROM java:openjdk-8-jdk  
  
RUN apt-get update && apt-get install -y --no-install-recommends unzip bash
openssh-client nodejs git ca-certificates fontconfig xvfb libpango1.0-0
libxss1 fonts-liberation libappindicator1 xdg-utils libgtk-3-0 lsb-release &&
rm -rf /var/lib/apt/lists/* && ln -s /usr/bin/nodejs /usr/bin/node  
  
ENV ACTIVATOR_VER 1.3.12  
RUN cd /opt \  
&& wget http://downloads.typesafe.com/typesafe-
activator/${ACTIVATOR_VER}/typesafe-activator-${ACTIVATOR_VER}-minimal.zip \  
&& unzip typesafe-activator-${ACTIVATOR_VER}-minimal.zip \  
&& ln -s /opt/activator-${ACTIVATOR_VER}-minimal /opt/activator \  
&& rm -f /opt/typesafe-activator-${ACTIVATOR_VER}-minimal.zip \  
&& chmod -R 775 /opt/activator/bin/  
  
ENV PATH=$PATH:/opt/activator/bin  
  
WORKDIR /src  
RUN activator new dummy play-java  
WORKDIR /src/dummy  
RUN activator help  
WORKDIR /src  
RUN rm -Rf dummy  
  
ENV PHANTOM_JS phantomjs-2.1.1-linux-x86_64  
  
RUN cd /opt \  
&& wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2 \  
&& tar xvjf $PHANTOM_JS.tar.bz2 \  
&& mv $PHANTOM_JS /usr/local/share \  
&& ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin  
  
RUN cd /opt \  
&& wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& dpkg -i google-chrome-stable_current_amd64.deb  
  
RUN cd /opt \  
&& wget
https://chromedriver.storage.googleapis.com/2.34/chromedriver_linux64.zip \  
&& unzip chromedriver_linux64.zip  
  
VOLUME /src  

