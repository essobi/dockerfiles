FROM ravellosystems/public-general-slave:latest  
  
  
RUN apt-get install -y nodejs npm  
RUN ln -s /usr/bin/nodejs /usr/bin/node  
RUN apt-get install -y zlib1g-dev ruby-dev ruby-bundler git wget curl
fontconfig subversion software-properties-common  
  
###ubuntu desktop  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install base utilities  
RUN apt-get -y update && apt-get -y -q install wget ca-certificates
xfonts-100dpi xfonts-75dpi xfonts-scalable xfonts-cyrillic  
  
# Prepare sources  
RUN wget -q -O - "https://dl-ssl.google.com/linux/linux_signing_key.pub" |
apt-key add -  
RUN echo "deb http://security.ubuntu.com/ubuntu precise-security main" >>
/etc/apt/sources.list  
RUN echo 'deb http://dl.google.com/linux/chrome/deb/ stable main' >>
/etc/apt/sources.list  
RUN echo "deb http://ppa.launchpad.net/ubuntu-mozilla-security/ppa/ubuntu
trusty main " >> /etc/apt/sources.list  
RUN apt-get -y update  
  
# Install utilities from sources  
RUN apt-get -y install libnss3-1d dbus google-chrome-stable firefox xvfb unzip
apparmor-utils x11vnc dbus-x11  
RUN apt-get -y update  
  
# # Download and copy the ChromeDriver to /usr/local/bin  
RUN cd /tmp  
RUN wget
"http://chromedriver.storage.googleapis.com/2.8/chromedriver_linux64.zip"  
RUN unzip chromedriver_linux64.zip  
RUN mv chromedriver /usr/local/bin  
RUN wget "http://selenium-release.storage.googleapis.com/2.45/selenium-server-
standalone-2.45.0.jar"  
RUN mv selenium-server-standalone-2.45.0.jar /usr/local/bin  
#RUN wget "http://mirror.pcbeta.com/google/chrome/deb/pool/main/g/google-
chrome-stable/google-chrome-stable_41.0.2272.76-1_amd64.deb"  
#RUN apt-get purge -y google-chrome-stable  
#RUN dpkg -i google-chrome-stable_41.0.2272.76-1_amd64.deb  
# Selenium port  
EXPOSE 4444 9222  
###end ubuntu desktop  
RUN npm install -g grunt-cli  
RUN npm install -g bower  
RUN gem install compass  
RUN npm install -g protractor  
RUN npm install -g karma-phantomjs-launcher  
RUN webdriver-manager update --standalone  
  
#Java 1.6  
RUN apt-get install -y openjdk-6-jre  
  
# Load scripts  
COPY bootstrap bootstrap  
RUN chmod +x -Rv bootstrap  
  
USER root  
ENV DISPLAY :10  
ENV LD_LIBRARY_PATH /usr/lib/x86_64-linux-gnu/  
  
# Standard SSH port  
EXPOSE 22  
# Selenium port  
EXPOSE 4444  
EXPOSE 5900  
EXPOSE 5901  
# Startup services when running the container  
CMD ["/bootstrap/init.sh"]  

