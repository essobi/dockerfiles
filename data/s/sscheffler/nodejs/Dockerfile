  
FROM sscheffler/jdk  
  
MAINTAINER Stefan Scheffler (stefan-scheffler@web.de)  
  
RUN apt-get update && \  
apt-get install -y ruby curl git gcc make g++ python  
  
RUN useradd -ms /bin/bash node  
ENV HOME /home/node  
ENV PATH $HOME/.linuxbrew/bin:$PATH  
  
USER node  
  
# install brew and perform formula update  
RUN ruby -e "$(curl -fsSL
https://raw.githubusercontent.com/Homebrew/linuxbrew/go/install)" && \  
brew doctor && \  
brew tap homebrew/dupes  
  
# install nodejs  
RUN brew install node  
  
#grunt  
RUN npm install -g grunt-cli  
USER root  

