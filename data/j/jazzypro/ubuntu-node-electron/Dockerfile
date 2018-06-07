FROM jazzypro/ubuntu-basic:14.04  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
#  
# Add repositories and update packages list  
#  
RUN curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -  
RUN apt-get update  
  
#  
# Install node.js and update NPM  
#  
RUN apt-get install -y nodejs  
RUN node -v  
RUN echo node version $(node -v) >> /root/soft_versions  
RUN npm -v  
RUN echo npm version $(node -v) >> /root/soft_versions  
  
#  
# Setup npm cache proxy  
#  
RUN npm config set proxy http://jazzy.pro:4011/  
RUN npm config set https-proxy http://jazzy.pro:4011/  
RUN npm config set strict-ssl false  
  
#  
# Install SASS/Compass  
#  
RUN apt-get install -y ruby ruby-dev  
RUN gem install sass compass  
RUN ruby -v  
RUN echo $(ruby -v) >> /root/soft_versions  
  
#  
# Install Gulp, Bower, LESS, Webpack  
#  
RUN npm install -g gulp  
RUN npm install -g bower  
RUN npm install -g less  
RUN npm install -g webpack  
  
#  
# Install Electron  
#  
RUN npm install -g electron  
RUN npm install -g electron-packager  
  
#  
# Install Wine  
#  
RUN dpkg --add-architecture i386  
RUN add-apt-repository -y ppa:ubuntu-wine/ppa  
RUN apt-get update  
RUN apt-get install -y wine1.8 winetricks  

