FROM gocd/gocd-agent  
  
MAINTAINER Abdulkadir Yaman <abdulkadiryaman@gmail.com>  
  
### installing packages  
RUN apt-add-repository ppa:brightbox/ruby-ng -y  
  
RUN apt-get update  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
ca-certificates \  
fonts-takao \  
gconf-service \  
gksu \  
libappindicator1 \  
libasound2 \  
libcurl3 \  
libgconf-2-4 \  
libnspr4 \  
libnss3 \  
libxss1 \  
libpango1.0-0 \  
build-essential \  
chrpath \  
libssl-dev \  
libxft-dev \  
libfreetype6 \  
libfreetype6-dev \  
libfontconfig1 \  
libfontconfig1-dev \  
pulseaudio \  
python-psutil \  
supervisor \  
wget \  
xbase-clients \  
xdg-utils \  
xvfb \  
firefox \  
ruby1.9.3 \  
freetds-dev \  
cowsay \  
zlib1g-dev \  
qt5-default \  
qt5-qmake \  
libqt5webkit5-dev \  
unzip  
  
RUN wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-1.9.8-linux-x86_64.tar.bz2  
RUN tar xvjf phantomjs-1.9.8-linux-x86_64.tar.bz2  
RUN mv phantomjs-1.9.8-linux-x86_64 /usr/local/share  
RUN ln -sf /usr/local/share/phantomjs-1.9.8-linux-x86_64/bin/phantomjs
/usr/local/bin  
RUN phantomjs --version  
RUN rm -rf phantomjs-1.9.8-linux-x86_64*  
  
RUN gem install bundler cucumber bson_ext --verbose  
  
RUN bundle config build.nokogiri --use-system-libraries  
  
RUN gem install nokogiri -v '1.6.6.2'  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
### installing packages END  
### installing chrome  
ADD https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
/chrome.deb  
  
RUN dpkg -i /chrome.deb && rm /chrome.deb  
  
RUN ln -s /lib/x86_64-linux-gnu/libudev.so.1 /lib/x86_64-linux-
gnu/libudev.so.0  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
VOLUME ["/home/chrome"]  
  
RUN useradd -m -G pulse-access chrome  
  
RUN ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]  
### installing chrome END  
### installing chrome driver  
RUN wget -N
https://chromedriver.storage.googleapis.com/2.15/chromedriver_linux64.zip -P
/tmp/  
RUN unzip /tmp/chromedriver_linux64.zip  
RUN chmod +x /tmp/chromedriver  
RUN mv /tmp/chromedriver /usr/bin/  
### installing chrome driver END  
### setting up localtime, go user privileges  
RUN ln -sf /usr/share/zoneinfo/Turkey /etc/localtime  
RUN echo "%go ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
ENV LANG en_US.UTF-8  
RUN locale-gen $LANG  
### setting up localtime, go user privileges, go-agent autoregister END  

