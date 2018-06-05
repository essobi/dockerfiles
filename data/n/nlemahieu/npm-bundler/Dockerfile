FROM ubuntu:16.04  
  
ARG UID=1001  
ARG GID=1001  
  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y curl && \  
curl -sL https://deb.nodesource.com/setup_6.x | bash - && \  
apt-get install -y nodejs fontforge ttfautohint && \  
apt-get install -y build-essential && \  
npm install -g grunt-cli \--save-dev && \  
npm install -g grunt-contrib-jshint \--save-dev && \  
npm install -g grunt-contrib-uglify \--save-dev && \  
npm install -g grunt-contrib-clean \--save-dev && \  
npm install -g grunt-contrib-concat \--save-dev && \  
npm install -g grunt-contrib-cssmin \--save-dev && \  
npm install -g grunt-contrib-less \--save-dev && \  
npm install -g grunt-shell \--save-dev && \  
npm install -g grunt-contrib-coffee \--save-dev && \  
npm install -g grunt-bower-task \--save-dev && \  
npm install -g grunt-contrib-symlink \--save-dev && \  
npm install -g grunt-symlink \--save-dev && \  
npm install -g grunt-contrib-copy \--save-dev && \  
npm install -g grunt-contrib-watch \--save-dev && \  
npm install -g grunt-webfont \--save-dev && \  
npm install -g bower \--save-dev && \  
npm install -g generator-angular \--save-dev && \  
npm install -g coffee-script \--save-dev && \  
apt-get install -y ruby-full && \  
gem install bundler && \  
ln -s /usr/bin/nodejs /usr/local/bin/node  
  
RUN export uid=$UID gid=$GID && \  
mkdir -p /home/developer/project && \  
echo "developer:x:$UID:$GID:Developer,,,:/home/developer:/bin/bash" >>
/etc/passwd && \  
echo "developer:x:$UID:" >> /etc/group && \  
echo "developer ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers && \  
chown $UID:$GID -R /home/developer  
  
USER developer  
ENV HOME /home/developer/project  
WORKDIR /home/developer/project  

