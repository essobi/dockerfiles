FROM ubuntu:14.04  
# based on docker image from https://github.com/killercentury/docker-jenkins-
dind  
MAINTAINER David Schlechtweg "david.schlechtweg@me.com"  
# global versions  
ENV DOCKER_COMPOSE_VERSION 1.14.0  
ENV NODEJS_VERSION 8.1.4  
ENV DOCKER_MACHINE_VERSION 0.12.2  
ENV SONARQUBE_VERSION 6.4  
ENV SONARQUBE_HOME /usr/local/sonarqube-$SONARQUBE_VERSION  
ENV RUBY_VERSION 2.0.0-p648  
  
# basic packages  
RUN apt-get update -qq && apt-get install -qqy \  
apt-transport-https \  
ca-certificates \  
curl \  
lxc \  
iptables \  
python \  
build-essential \  
git \  
g++ \  
openssl  
  
# install RVM, Ruby, Bundler, Sass  
RUN curl -L https://get.rvm.io | bash -s stable  
RUN /bin/bash -l -c "rvm requirements"  
RUN /bin/bash -l -c "rvm install ${RUBY_VERSION}"  
RUN /bin/bash -l -c "gem install bundler --no-ri --no-rdoc"  
RUN /bin/bash -l -c "gem install sass --no-ri --no-rdoc"  
ENV
PATH=$PATH:/usr/local/rvm/gems/ruby-${RUBY_VERSION}/bin:/usr/local/rvm/rubies/ruby-${RUBY_VERSION}/bin:/usr/local/rvm/rubies/ruby-${RUBY_VERSION}/lib/ruby/gems/${RUBY_VERSION}/bin  
ENV
GEM_PATH=/usr/local/rvm/gems/ruby-${RUBY_VERSION}:/usr/local/rvm/rubies/ruby-${RUBY_VERSION}:/usr/local/rvm/rubies/ruby-${RUBY_VERSION}/lib/ruby/gems/${RUBY_VERSION}  
  
  
# installing java jdk  
RUN apt-get update && \  
apt-get install software-properties-common -y && \  
add-apt-repository ppa:webupd8team/java -y && \  
apt-get update && \  
echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-
selections && \  
apt-get install oracle-java8-installer -y  
  
# nightwatch and selenium headless  
# from https://github.com/dockerfile/chrome/blob/master/Dockerfile  
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-
key add - && \  
echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >
/etc/apt/sources.list.d/google.list && \  
apt-get update && \  
apt-get install -y google-chrome-stable xvfb  
  
#  
# docker  
#  
# install docker core  
RUN curl -sSL https://get.docker.com/ | sh  
  
# install the wrapper script from
https://raw.githubusercontent.com/docker/docker/master/hack/dind.  
ADD ./dind /usr/local/bin/dind  
RUN chmod +x /usr/local/bin/dind  
  
ADD ./wrapdocker /usr/local/bin/wrapdocker  
RUN chmod +x /usr/local/bin/wrapdocker  
  
# docker compose  
RUN curl -L
https://github.com/docker/compose/releases/download/${DOCKER_COMPOSE_VERSION}/docker-
compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose  
RUN chmod +x /usr/local/bin/docker-compose  
  
# docker machine  
RUN curl -L
https://github.com/docker/machine/releases/download/v${DOCKER_MACHINE_VERSION}/docker-
machine-`uname -s`-`uname -m` > /usr/local/bin/docker-machine  
RUN chmod +x /usr/local/bin/docker-machine  
  
# Define additional metadata for our image.  
VOLUME /var/lib/docker  
  
#  
# jenkins  
#  
# install jenkins  
RUN wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | apt-key
add -  
RUN sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ >
/etc/apt/sources.list.d/jenkins.list'  
RUN apt-get update && apt-get install -y zip supervisor jenkins && rm -rf
/var/lib/apt/lists/*  
RUN usermod -a -G docker jenkins  
ENV JENKINS_HOME /var/lib/jenkins  
VOLUME /var/lib/jenkins  
# adding initial jenkins plugins  
#RUN /usr/local/bin/install-plugins.sh git nodejs docker-build-step  
#  
# nodejs  
#  
# create dir for npm cache (run npm config set cache /var/npm/cache)  
RUN mkdir /var/npm && chown jenkins:docker /var/npm  
  
# nodejs  
RUN mkdir /nodejs && curl
http://nodejs.org/dist/v${NODEJS_VERSION}/node-v${NODEJS_VERSION}-linux-x64.tar.gz
| tar xvzf - -C /nodejs --strip-components=1  
ENV PATH=$PATH:/nodejs/bin  
# needed global npm deps  
RUN npm install -g node-gyp && \  
npm install -g gulp && \  
npm install -g nightwatch && \  
npm install -g nightwatch-html-reporter && \  
npm install -g grunt-cli && \  
npm install -g bower && \  
npm install --unsafe-perm -g azure-cli && \  
azure telemetry --disable  
  
#  
# sonarqube  
#  
# download and unzip  
RUN wget -O /tmp/SQ.zip
http://sonarsource.bintray.com/Distribution/sonarqube/sonarqube-$SONARQUBE_VERSION.zip
\  
&& unzip -o /tmp/SQ.zip -d /usr/local/ \  
&& rm /tmp/SQ.zip  
  
# copy properties  
VOLUME "$SONARQUBE_HOME/data"  
VOLUME "$SONARQUBE_HOME/conf"  
COPY ./sonar.properties $SONARQUBE_HOME/conf/  
  
#  
# process manager  
#  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
EXPOSE 8080 9000  
CMD ["/usr/bin/supervisord"]  

