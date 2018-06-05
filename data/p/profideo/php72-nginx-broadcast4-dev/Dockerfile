FROM profideo/php72-nginx-broadcast4:broadcast4-php72  
  
RUN apt-get update && apt-get install -y unzip  
  
RUN docker-php-ext-install pcntl  
COPY files/opcache.ini $PHP_INI_DIR/conf.d/  
  
RUN echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable
main" | tee /etc/apt/sources.list.d/google-chrome.list  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN apt-get update && apt-get install -y google-chrome-stable  
  
RUN echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true | /usr/bin/debconf-set-selections  
RUN echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" |
tee /etc/apt/sources.list.d/webupd8team-java.list  
RUN echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty
main" | tee -a /etc/apt/sources.list.d/webupd8team-java.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886  
RUN apt-get update && apt-get install oracle-java8-installer -y && apt-get
clean  
RUN echo "JAVA_HOME=/usr/lib/jvm/java-8-oracle" >> /etc/environment  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
ADD https://chromedriver.storage.googleapis.com/2.36/chromedriver_linux64.zip
/opt/  
RUN mkdir /opt/chromedriver  
RUN unzip -d /opt/chromedriver /opt/chromedriver_linux64.zip  
RUN echo "PATH=${PATH}:/opt/chromedriver" >> /etc/environment  
ENV PATH="${PATH}:/opt/chromedriver"  
ADD https://selenium-release.storage.googleapis.com/3.11/selenium-server-
standalone-3.11.0.jar /opt/  
RUN chmod o+r /opt/selenium-server-standalone-3.11.0.jar  

