FROM jenkins:2.19.3  
USER root  
  
RUN apt-get update \  
&& apt-get install -y sudo curl python python-dev python-pip ruby \  
&& rm -rf /var/lib/apt/lists/*  
RUN echo "jenkins ALL=NOPASSWD: ALL" >> /etc/sudoers  
  
RUN curl -sSL https://get.docker.com/ | /bin/sh  
RUN usermod -aG docker jenkins  
  
######## INSTALL NODE #########  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 6.3.0  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
######## INSTALL METEOR ########  
RUN curl -sSL https://install.meteor.com/ | /bin/sh  
  
######## INSTALL DOCKER-COMPOSE ########  
RUN curl -L https://github.com/docker/compose/releases/download/1.7.1/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
RUN docker-compose --version  
  
######## INSTALL NPM PACKAGES ########  
RUN npm install -g typescript@2.3.4 mocha@2.5.3 typings babel-istanbul@0.11.0
typedoc  
  
######## INSTALL ANSIBLE ########  
RUN apt-get update \  
&& apt-get install -y libffi6 libffi-dev libssl-dev && rm -rf
/var/lib/apt/lists/*  
RUN apt-get --purge remove -y python-cffi  
RUN pip install --upgrade cffi setuptools cryptography ansible markupsafe &&
gem install pry && mkdir /etc/ansible && chown -hR jenkins /etc/ansible  
  
COPY plugins.txt /usr/share/jenkins/plugins.txt  
RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt  
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state  
USER jenkins

