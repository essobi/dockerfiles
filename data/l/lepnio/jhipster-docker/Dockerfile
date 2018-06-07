# DOCKER-VERSION 1.5.0  
FROM dockerfile/java:oracle-java8  
MAINTAINER Etienne Peiniau <etienne.peiniau@gmail.com>  
  
# set up  
RUN chmod 777 /tmp  
RUN apt-get update  
  
# install maven  
ENV MAVEN_VERSION 3.2.5  
RUN curl -sSL
http://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn  
  
ENV MAVEN_HOME /usr/share/maven  
  
# install node.js  
RUN gpg --keyserver pool.sks-keyservers.net --recv-keys
7937DFD2AB06298B2293C3187D33FF9D0246406D
114F43EE0176B71C7BC219DD50A3051F888C628D  
  
ENV NODE_VERSION 0.12.0  
ENV NPM_VERSION 2.5.0  
RUN curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "http://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --verify SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.gz\$" SHASUMS256.txt.asc |
sha256sum -c - \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
# install grunt, yeoman and JHipster  
RUN npm install -g yo  
RUN npm install -g grunt-cli  
RUN npm install -g bower  
RUN npm install -g generator-jhipster@2.5.2  
  
# install sass and compass  
RUN apt-get install -y ruby1.9.1-full  
RUN gem install sass  
RUN gem install compass  
  
# create jhipster user  
RUN groupadd jhipster && useradd jhipster -s /bin/bash -m -g jhipster  
ENV HOME /home/jhipster  
USER jhipster  
  
# expose ports  
EXPOSE 8080  
EXPOSE 9000  
# yeamon default entrypoint  
WORKDIR /data  
CMD ["yo"]  

