FROM enonic/java8  
  
MAINTAINER Jørgen Sivesind <jsi@enonic.com>  
  
USER root  
  
# Setup  
RUN mkdir /data  
VOLUME /data  
ENV HOME=/data  
  
# Tools  
RUN apt-get update \  
&& apt-get install -y curl zip unzip make \  
&& apt-get clean  
  
# NodeJS  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
# Gradle  
ENV GRADLE_VERSION=4.6  
ENV GRADLE_HOME=/opt/gradle  
RUN wget --no-check-certificate --no-cookies
https://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip \  
&& unzip gradle-${GRADLE_VERSION}-bin.zip -d /opt \  
&& ln -s /opt/gradle-${GRADLE_VERSION} /opt/gradle \  
&& rm -f gradle-${GRADLE_VERSION}-bin.zip  
RUN update-alternatives --install "/usr/bin/gradle" "gradle"
"/opt/gradle/bin/gradle" 1 && \  
update-alternatives --set "gradle" "/opt/gradle/bin/gradle"  
  
# Chrome  
ENV REV=530372  
RUN apt-get update -qqy \  
&& apt-get -qqy install libnss3 libnss3-tools libfontconfig1 wget ca-
certificates apt-transport-https inotify-tools \  
libpangocairo-1.0-0 libx11-xcb-dev libxcomposite-dev libxcursor1 libxdamage1
libxi6 libgconf-2-4 libxtst6 libcups2-dev \  
libxss-dev libxrandr-dev libasound2-dev libatk1.0-dev libgtk-3-dev ttf-
ancient-fonts chromium-codecs-ffmpeg-extra \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
RUN wget -q -O chrome.zip https://commondatastorage.googleapis.com/chromium-
browser-snapshots/Linux_x64/$REV/chrome-linux.zip \  
&& unzip chrome.zip \  
&& rm chrome.zip \  
&& ln -s $PWD/chrome-linux/chrome /usr/local/bin/chrome  
  
# Chrome webdriver  
ARG CHROME_DRIVER_VERSION="latest"  
RUN CD_VERSION=$(if [ ${CHROME_DRIVER_VERSION:-latest} = "latest" ]; then echo
$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE); else
echo $CHROME_DRIVER_VERSION; fi) \  
&& echo "Using chromedriver version: "$CD_VERSION \  
&& wget --no-verbose -O /tmp/chromedriver_linux64.zip
https://chromedriver.storage.googleapis.com/$CD_VERSION/chromedriver_linux64.zip
\  
&& rm -rf /opt/selenium/chromedriver \  
&& unzip /tmp/chromedriver_linux64.zip -d /opt/selenium \  
&& rm /tmp/chromedriver_linux64.zip \  
&& mv /opt/selenium/chromedriver /opt/selenium/chromedriver-$CD_VERSION \  
&& chmod 755 /opt/selenium/chromedriver-$CD_VERSION \  
&& ln -fs /opt/selenium/chromedriver-$CD_VERSION /usr/local/bin/chromedriver  

