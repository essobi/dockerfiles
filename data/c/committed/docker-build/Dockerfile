FROM committed/java  
MAINTAINER Committed Software <docker@committed.software>  
  
ENV MAVEN_VERSION 3.3.9  
ENV NODE_VERSION 5  
# Install nodejs, Maven, git, build-essentials  
RUN apt-get update \  
&& curl -fsSL
https://archive.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz | tar xzf - -C /usr/share \  
&& mv /usr/share/apache-maven-$MAVEN_VERSION /usr/share/maven \  
&& ln -s /usr/share/maven/bin/mvn /usr/bin/mvn \  
&& curl -sL https://deb.nodesource.com/setup_$NODE_VERSION.x | bash - \  
&& apt-get -y install nodejs git build-essential \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV MAVEN_HOME /usr/share/maven  
  
# For convenience we expose the src, .m2, etc directory, so it can be provided
by the user  
RUN mkdir /src \  
&& mkdir /.m2 \  
&& mkdir /.npm \  
&& npm config set cache /.npm  
ENV MAVEN_OPTS -Dmaven.repo.local=/.m2  
  
VOLUME /src  
VOLUME /.npm  
VOLUME /.m2  
  
WORKDIR /src  
  
# Install global node packages  
RUN npm install -g webpack \  
&& npm install -g gulp \  
&& npm install -g bower  
  
ENTRYPOINT ["/bin/bash"]  
CMD []

