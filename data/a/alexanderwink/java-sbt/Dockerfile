FROM java:openjdk-8-jdk  
  
RUN echo "deb http://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823  
  
RUN apt-get update && apt-get install -y --no-install-recommends unzip bash
openssh-client nodejs git ca-certificates fontconfig xvfb libpango1.0-0
libxss1 fonts-liberation libappindicator1 xdg-utils libgtk-3-0 lsb-release
libnss3 sbt && rm -rf /var/lib/apt/lists/* && ln -s /usr/bin/nodejs
/usr/bin/node  
  
COPY play /tmp/play  
  
RUN cd /tmp/play && sbt compile && rm -Rf /tmp/play  
  
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
https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip \  
&& unzip chromedriver_linux64.zip  
  
VOLUME /src  

