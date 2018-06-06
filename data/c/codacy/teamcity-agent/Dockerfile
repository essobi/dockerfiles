FROM jetbrains/teamcity-minimal-agent:latest  
  
MAINTAINER Kateryna Shlyakhovetska <shkate@jetbrains.com>  
  
LABEL dockerImage.teamcity.version="latest" \  
dockerImage.teamcity.buildNumber="latest"  
  
RUN locale-gen en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
ENV RUBY_VERSION 2.3.1  
ENV NODE_VERSION 7.0.0  
  
ENV RBENV_HOME "/root/.rbenv"  
ENV NODENV_HOME "/root/.nodenv"  
ENV COMPOSER_HOME "/root/.composer"  
  
ENV PATH
"$RBENV_HOME/bin:$RBENV_HOME/shims:$NODENV_HOME/bin:$NODENV_HOME/shims:$COMPOSER_HOME/bin:$PATH"  
  
RUN \  
groupadd -g 2004 docker && \  
adduser --disabled-password --gecos "" \--uid 2004 \--gid 2004 docker && \  
gpasswd -a docker docker && \  
gpasswd -a root docker  
  
RUN apt-get update -y && \  
apt-get install -y software-properties-common zip mercurial apt-transport-
https ca-certificates && \  
add-apt-repository ppa:openjdk-r/ppa && \  
echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list && \  
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823 && \  
add-apt-repository ppa:ondrej/php && \  
add-apt-repository ppa:git-core/ppa && \  
apt-get update -y && \  
apt-get install -y git autoconf bison build-essential libssl-dev libyaml-dev
libreadline6-dev zlib1g-dev libncurses5-dev libffi-dev libgdbm3 libgdbm-dev &&
\  
\  
echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config && \  
git config --global core.quotepath false && \  
git config --global core.packedGitLimit 512m && \  
git config --global core.packedGitWindowSize 512m && \  
git config --global pack.deltaCacheSize 2047m && \  
git config --global pack.packSizeLimit 2047m && \  
git config --global pack.windowMemory 2047m && \  
apt-get -y install apparmor libdevmapper1.02.1 && \  
apt-get install -y python3 python3-dev python3-pip libffi-dev libssl-dev
libxml2-dev libxslt1-dev libjpeg8-dev zlib1g-dev && \  
python3 -m pip install --upgrade pip && \  
python3 -m pip install --upgrade aws && \  
python3 -m pip install --upgrade ansible && \  
python3 -m pip install --upgrade boto && \  
python3 -m pip install --upgrade docker-compose && \  
python3 -m pip install --upgrade metrics===0.2.6 && \  
python3 -m pip install --upgrade radon===1.4.2 && \  
\  
apt-get install -y openjdk-8-jdk && \  
apt-get install -y sbt && \  
\  
apt-get install -y php5-dev php5-cli && \  
curl -sS https://getcomposer.org/installer | php && \  
mv composer.phar /bin/composer && \  
composer global require "pdepend/pdepend=2.3.2" && \  
\  
git clone https://github.com/rbenv/rbenv.git $RBENV_HOME && \  
git clone https://github.com/rbenv/ruby-build.git $RBENV_HOME/plugins/ruby-
build && \  
eval "$(rbenv init -)" && \  
rbenv install $RUBY_VERSION && \  
rbenv global $RUBY_VERSION && \  
echo 'eval "$(rbenv init -)"' >> /root/.bashrc && \  
gem install bundler && \  
gem install sass && \  
\  
git clone https://github.com/nodenv/nodenv.git $NODENV_HOME && \  
git clone https://github.com/nodenv/node-build.git $NODENV_HOME/plugins/node-
build && \  
eval "$(nodenv init -)" && \  
nodenv install -s $NODE_VERSION && \  
nodenv global $NODE_VERSION && \  
echo 'eval "$(nodenv init -)"' >> /root/.bashrc && \  
npm install -g cloc && \  
\  
apt-get clean all  

