FROM klikatech/teamcity-agent-base  
  
MAINTAINER Eugene Volchek <evolchek@klika-tech.com>  
  
USER root  
  
RUN apt-get update \  
&& apt-get install -y rsync bzip2 ruby-full build-essential ant \  
php5-common php5-mysql php5-pgsql php5-cli php5-dev php5-curl php5-memcached
php5-gd \  
zip nodejs groff less python python-pip apt-transport-https jq \  
libappindicator1 libindicator7 libpango1.0-0 fonts-liberation xdg-utils\  
&& wget https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb \  
&& dpkg --force-depends -i google-chrome*.deb \  
&& apt-get install -y -f \  
&& wget https://dl.google.com/android/android-sdk_r24.2-linux.tgz \  
&& tar -xfz android-sdk_r24.2-linux.tgz \  
&& cd android-sdk-linux \  
&& tools/android update sdk \  
&& cd .. \  
&& mkdir -p /usr/share/maven \  
&& curl -fsSL http://apache.osuosl.org/maven/maven-3/3.3.9/binaries/apache-
maven-3.3.9-bin.tar.gz | tar -xzC /usr/share/maven --strip-components=1 \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
&& apt-get install -y xvfb \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 642AC823 \  
&& apt-get update \  
&& apt-get install -y nodejs sbt \  
&& npm install -g npm@next \  
&& npm install -g bower \  
&& npm install -g grunt-cli \  
&& npm install -g webpack \  
&& curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& gem install sass \  
&& gem install compass \  
&& gem install jekyll \  
&& curl -sSL https://get.docker.com/ | sh \  
&& pip install awscli \  
&& apt-get -y autoremove && apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV MAVEN_HOME /usr/share/maven  
  
USER teamcity  

