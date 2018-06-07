FROM openjdk:7  
MAINTAINER Sathwik B P  
  
ENV NODE_VERSION 6.6.0  
ENV MAVEN_VERSION 3.3.9  
ENV PHANTOSJS_VERSION 2.1.1  
ENV WORKSPACE /workspace  
ENV PATH /usr/local/bin:$PATH  
  
#install nodejs  
RUN mkdir -p /opt/node \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& tar -Jxf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /opt/node --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" \  
&& update-alternatives --install /usr/local/bin/node node /opt/node/bin/node 1
\  
&& update-alternatives --install /usr/local/bin/npm npm /opt/node/bin/npm 1  
  
ENV PATH /opt/node/bin:$PATH  
  
RUN npm install -g minimatch@3.0.2 \  
&& npm install -g bower \  
&& npm install -g gulp  
  
RUN update-alternatives --install /usr/local/bin/bower bower
/opt/node/bin/bower 1 \  
&& update-alternatives --install /usr/local/bin/gulp gulp /opt/node/bin/gulp 1  
  
#install phontomjs  
RUN curl -SLO
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOSJS_VERSION-
linux-x86_64.tar.bz2 \  
&& tar -jxf "phantomjs-$PHANTOSJS_VERSION-linux-x86_64.tar.bz2" -C /usr/local
\--strip-components=1 \  
&& rm "phantomjs-$PHANTOSJS_VERSION-linux-x86_64.tar.bz2" \  
&& ln -s /usr/local/phantomjs /usr/bin/phatomjs  
  
# install maven  
RUN mkdir -p /opt/maven /opt/maven/ref \  
&& curl -SLO
http://apache.osuosl.org/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz \  
&& tar -xf "apache-maven-$MAVEN_VERSION-bin.tar.gz" -C /opt/maven --strip-
components=1 \  
&& rm "apache-maven-$MAVEN_VERSION-bin.tar.gz" \  
&& update-alternatives --install /usr/local/bin/mvn mvn /opt/maven/bin/mvn 1  
  
ENV PATH /opt/maven/bin:$PATH  
  
ENV MAVEN_HOME /opt/maven  
  
# make /tmp available to all users.  
RUN chmod 777 -R /tmp && chmod o+t -R /tmp  
  
VOLUME /workspace  
WORKDIR /workspace  
  
ENTRYPOINT [ "gulp" ]

