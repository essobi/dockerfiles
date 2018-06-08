FROM jenkins/jenkins:lts  
  
USER root  
  
RUN \  
apt update && \  
apt install -y \  
apt-transport-https \  
ca-certificates \  
gnupg2 \  
software-properties-common \  
zip \  
autoconf \  
automake \  
libtool \  
make \  
curl \  
rsync \  
build-essential \  
git \  
libkrb5-dev \  
netcat-openbsd && \  
apt-get clean autoclean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add - && \  
echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
  
RUN \  
apt update && \  
apt install -y \  
yarn && \  
apt-get clean autoclean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN \  
wget -q https://get.docker.com/builds/Linux/x86_64/docker-1.9.1 && \  
mv /docker-1.9.1 /usr/local/bin/docker && \  
chmod a+x /usr/local/bin/docker  
  
ENV N_PREFIX /usr/local/n-install  
RUN \  
curl -L https://git.io/n-install | bash -s -- -y lts  
ENV PATH $N_PREFIX:$N_PREFIX/bin:$PATH  
  
RUN \  
npm install -g \  
node-gyp \  
polymer-cli \  
gulp-cli \  
bower \  
mocha \  
nightwatch \  
eslint \  
esdoc  
  
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt  
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod a+x /entrypoint.sh  
  
ADD /jobs /jobs  
#COPY groovy/*.groovy /usr/share/jenkins/ref/init.groovy.d/  
RUN chown -R jenkins:jenkins /var/jenkins_home/  
  
USER jenkins  
  
ENTRYPOINT ["/bin/tini", "--", "/entrypoint.sh"]  

