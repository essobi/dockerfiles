FROM ubuntu:14.04  
MAINTAINER Cedric Lamoriniere <cedric.lamoriniere@gmail.com>  
  
# Install.  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y software-properties-common && \  
apt-get install -y byobu curl git htop man unzip vim wget && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Python.  
RUN \  
apt-get update && \  
apt-get install -y python python-dev python-pip python-virtualenv && \  
rm -rf /var/lib/apt/lists/*  
  
# Install Node.js  
RUN \  
cd /tmp && \  
wget http://nodejs.org/dist/node-latest.tar.gz && \  
tar xvzf node-latest.tar.gz && \  
rm -f node-latest.tar.gz && \  
cd node-v* && \  
./configure && \  
CXX="g++ -Wno-unused-local-typedefs" make && \  
CXX="g++ -Wno-unused-local-typedefs" make install && \  
cd /tmp && \  
rm -rf /tmp/node-v* && \  
npm install -g npm && \  
printf '\n# Node.js\nexport PATH="node_modules/.bin:$PATH"' >> /root/.bashrc  
  
# Install Bower & Gulp  
RUN npm install -g bower gulp node-sass  
  
# Installing SASS/Compass  
RUN apt-get install software-properties-common  
RUN apt-add-repository ppa:brightbox/ruby-ng  
RUN apt-get update  
RUN apt-get install -y ruby-full rubygems-integration  
RUN gem install sass  
RUN gem install compass  
  
RUN sudo apt-get install -y build-essential chrpath libssl-dev libxft-dev
libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev  
  
ENV PHANTOM_JS="phantomjs-1.9.8-linux-x86_64"  
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/$PHANTOM_JS.tar.bz2
&& \  
tar xvjf $PHANTOM_JS.tar.bz2 && \  
mv $PHANTOM_JS /usr/local/share && \  
ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin  
  
ENV PHANTOMJS_BIN=/usr/local/bin/phantomjs  
  
# install chrome  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - &&\  
sh -c 'echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >>
/etc/apt/sources.list.d/google.list' &&\  
sudo apt-get update &&\  
sudo apt-get install -y google-chrome-stable  
  
# Define working directory.  
WORKDIR /data  
  
VOLUME ["/data"]  
  
# expose gulp serve port  
EXPOSE 3000  
# expose karma port  
EXPOSE 9876  
# Define default command.  
CMD ["bash"]  

