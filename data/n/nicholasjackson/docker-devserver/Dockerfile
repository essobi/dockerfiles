FROM ubuntu:latest  
  
MAINTAINER Nic Jackson <nicholas.jackson@marks-and-spencer.com>  
  
# default exposed webserver port  
EXPOSE 8000  
EXPOSE 9090  
# live refresh port for node  
EXPOSE 35729  
VOLUME /src  
  
RUN sudo apt-get update  
  
RUN sudo echo y | apt-get install git  
  
RUN sudo echo y | apt-get install default-jre  
  
# install xvfb  
RUN echo y | sudo apt-get install xfonts-100dpi xfonts-75dpi xfonts-scalable
xfonts-cyrillic  
RUN echo y | sudo apt-get install xvfb  
  
# install firefox  
RUN echo y | sudo apt-get install firefox  
  
# install chrome  
RUN echo y | sudo apt-get install wget  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo
apt-key add -  
RUN sudo sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main"
>> /etc/apt/sources.list.d/google.list'  
RUN sudo apt-get update  
RUN echo y | sudo apt-get install google-chrome-stable  
  
# install phantomjs  
RUN echo y | sudo apt-get install phantomjs  
  
# install ruby and SASS gem required to build SASS from grunt  
RUN echo y | sudo apt-get install ruby  
RUN echo y | sudo apt-get install ruby-dev  
RUN echo y | sudo apt-get install build-essential  
RUN gem install compass  
  
RUN echo y | sudo apt-get install nodejs  
RUN echo y | sudo apt-get install npm  
RUN sudo ln -s /usr/bin/nodejs /usr/bin/node  
RUN npm install -g bower  
RUN npm install -g grunt-cli  
RUN npm install -g yo generator-fluxible  
RUN npm install -g react-tools  
  
# set the environment variable for the display  
ENV DISPLAY 99  
# start xvb on screen 99  
CMD ["/sbin/start-stop-daemon --start --quiet --pidfile
/tmp/custom_xvfb_99.pid --make-pidfile --background --exec /usr/bin/Xvfb --
:99 -ac -screen 0 1280x1024x16"]  

