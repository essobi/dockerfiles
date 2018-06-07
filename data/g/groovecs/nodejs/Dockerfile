# Copyright (c) 2012-2016 Codenvy, S.A.  
# All rights reserved. This program and the accompanying materials  
# are made available under the terms of the Eclipse Public License v1.0  
# which accompanies this distribution, and is available at  
# http://www.eclipse.org/legal/epl-v10.html  
# Contributors:  
# Codenvy, S.A. - initial API and implementation  
FROM eclipse/stack-base:debian  
  
RUN sudo apt-get update && \  
sudo apt-get -y install build-essential libkrb5-dev gcc make ruby-full
rubygems debian-keyring python2.7 && \  
sudo gem install --no-rdoc --no-ri sass -v 3.4.22 && \  
sudo gem install --no-rdoc --no-ri compass && \  
sudo apt-get clean && \  
sudo apt-get -y autoremove && \  
sudo apt-get -y clean && \  
sudo rm -rf /var/lib/apt/lists/*  
  
RUN wget -qO- https://deb.nodesource.com/setup_7.x | sudo -E bash -  
  
ENV Install NodeJS  
RUN sudo apt update && sudo apt -y install nodejs  
  
ENV Updating to latest NodeJS  
RUN sudo npm cache clean -f && sudo npm install -g n && sudo n stable  
  
ENV Install Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add - &&
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee
/etc/apt/sources.list.d/yarn.list && sudo apt-get update && sudo apt-get
install yarn  
  
EXPOSE 1337 3000 4200 5000 9000 8003  
ENV Install developer workspace  
RUN sudo npm install --unsafe-perm -g gulp bower grunt grunt-cli yo yeoman-
generator generator-angular generator-karma generator-webapp polymer-cli  
LABEL che:server:8003:ref=angular che:server:8003:protocol=http
che:server:3000:ref=node-3000 che:server:3000:protocol=http
che:server:9000:ref=node-9000 che:server:9000:protocol=http  

