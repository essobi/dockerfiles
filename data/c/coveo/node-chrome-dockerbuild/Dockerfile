FROM node:8  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add -  
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/
stable main" >> /etc/apt/sources.list.d/google.list'  
RUN sh -c 'echo "deb http://ftp.debian.org/debian jessie-backports main" >>
/etc/apt/sources.list.d/backport.list'  
  
RUN apt-get update  
RUN apt-get install -y google-chrome-unstable  
  
RUN apt-get install -yq libgconf-2-4  
RUN apt-get install -y make build-essential libssl-dev zlib1g-dev  
RUN apt-get install -y libbz2-dev libreadline-dev libsqlite3-dev wget curl
llvm  
RUN apt-get install -y libncurses5-dev libncursesw5-dev xz-utils tk-dev  
  
RUN apt-get install -y -t jessie-backports openjdk-8-jdk

