FROM codeamatic/teamcity-agent-bare:jdk8  
  
# Build dependencies  
RUN apt-get update \  
&& apt-get -y install software-properties-common lxc \  
&& apt-get -y install rsync bzip2 build-essential \  
&& apt-get -y install zip \  
# Install Node using PPA in order to access latest versions of Node  
&& curl -sL https://deb.nodesource.com/setup_6.x | sudo bash - \  
&& apt-get -y install nodejs \  
# PHP Tools  
&& apt-get -y install php5-cli \  
&& apt-get -y install php5-curl \  
&& curl -sS https://getcomposer.org/installer | sudo php -- --install-
dir=/usr/local/bin --filename=composer \  
# Python Tools  
&& apt-get install -y python-pip python-dev \  
# Frontend tools  
&& npm install -g npm@latest \  
&& npm install -g bower \  
&& npm install -g grunt-cli \  
&& npm install -g npm-cache \  
&& apt-get install -y fontforge \  
# Java Tools  
&& apt-get -y install maven \  
# Ruby  
&& apt-get update \  
&& apt-get -y install ruby-full libssl-dev \  
&& gem install sass \  
&& gem install compass \  
# Chrome Dependencies  
&& apt-get -y install libxss1 libappindicator1 libindicator7 gdebi  
  
# Chrome Install  
RUN wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb  
RUN apt-get update && apt-get install -f  
RUN gdebi --non-interactive google-chrome*.deb  
  
# Gradle  
ENV GRADLE_VERSION=3.4  
ENV GRADLE_HOME=/opt/gradle/latest  
ENV PATH=$PATH:$GRADLE_HOME/bin  
  
RUN wget
http://downloads.gradle.org/distributions/gradle-${GRADLE_VERSION}-all.zip  
RUN unzip -oq ./gradle-${GRADLE_VERSION}-all.zip -d /opt/gradle  
RUN ln -sfnv gradle-${GRADLE_VERSION} /opt/gradle/latest  
  
RUN gradle -v  
  
# Clean up  
RUN apt-get -y autoremove && apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

