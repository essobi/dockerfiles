# Dockerfile to build hoopla/hoopla-docker-scala-base  
FROM evarga/jenkins-slave  
MAINTAINER Halvor Granskogen Bjørnstad <halvor@hoopla.no>  
  
# Install python2.7 and python-pip, soome python dependencies and pip  
RUN apt-get update && \  
apt-get -y install python2.7 swig libpq-dev python-dev libffi-dev wget curl
jgit-cli && \  
wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py && \  
python /tmp/get-pip.py && \  
pip install sh logging setuptools awscli  
  
# Install docker-CLI binary. Version 1.1.2 bc. of newest ubuntu repo version  
ADD https://get.docker.com/builds/Linux/x86_64/docker-1.7.1
/usr/local/bin/docker  
RUN chmod +x /usr/local/bin/docker && \  
chmod u+w /etc/sudoers && \  
echo "%jenkins ALL=(ALL:ALL) NOPASSWD:ALL" >> /etc/sudoers && \  
chmod u-w /etc/sudoers && \  
visudo --check  
  
# Compile git with openssl (not gnutls)  
RUN apt-get update && \  
apt-get install -y build-essential fakeroot dpkg-dev && \  
mkdir -p /opt/git-openssl && \  
cd /opt/git-openssl && \  
apt-get source -y git && \  
apt-get build-dep -y git && \  
apt-get install -y libcurl4-openssl-dev && \  
dpkg-source -x git_*.dsc && \  
cd git* && \  
./configure --prefix=/opt && \  
make && \  
ln -s /opt/git-openssl/git-*/bin-wrappers/git /usr/bin/git  
  
# Install sbt  
RUN wget https://dl.bintray.com/sbt/debian/sbt-0.13.11.deb && \  
dpkg -i sbt-0.13.11.deb && \  
rm sbt-0.13.11.deb && \  
apt-get update && apt-get install -y sbt  
  
# Install Java.  
RUN \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
# Define commonly used JAVA_HOME variable  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
  
# Node stuff:  
RUN curl -o\-
https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | sudo -E
bash  
  
# jq!  
RUN apt-get update && apt-get -y install jq  
  
# Ruby stuff  
RUN apt-add-repository -y ppa:brightbox/ruby-ng && \  
apt-get update && \  
apt-get -y install ruby2.2 && \  
gem install bundler  
  
ENV NVM_DIR /usr/local/nvm  
ENV NODE_VERSION 6.9.0  
RUN curl https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh |
bash \  
&& . $NVM_DIR/nvm.sh && nvm install $NODE_VERSION && nvm use $NODE_VERSION &&
nvm alias default $NODE_VERSION && nvm use default  
  
ENV NODE_PATH $NVM_DIR/versions/node/v$NODE_VERSION/lib/node_modules  
ENV PATH $NVM_DIR/versions/node/v$NODE_VERSION/bin:$PATH  
  
RUN echo $PATH  
RUN npm install -g dredd  
  
# psql for connecting to postgresql  
RUN apt-get update && \  
apt-get -y install postgresql-client-9.3  
  
RUN apt-get update && \  
apt-get -y install redis-tools  

