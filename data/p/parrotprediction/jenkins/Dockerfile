FROM jenkins:1.642.2  
USER root  
  
ENV PHANTOMJS_VERSION 2.1.1  
ENV MAVEN_VERSION 3.3.3  
ENV MAVEN_HOME /usr/share/maven  
  
RUN apt-get update && apt-get install -y bzip2 curl git unzip  
  
#============================  
# Maven  
#============================  
RUN curl -SL
"http://ftp.ps.pl/pub/apache/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz" -o maven.tar.gz \  
&& curl -SL
"http://www.apache.org/dist/maven/maven-3/$MAVEN_VERSION/binaries/apache-
maven-$MAVEN_VERSION-bin.tar.gz.asc" -o maven.tar.gz.asc \  
&& gpg --keyserver pgpkeys.mit.edu --recv-key BB617866 \  
&& gpg --verify maven.tar.gz.asc maven.tar.gz \  
&& mkdir -p $MAVEN_HOME \  
&& tar -xf maven.tar.gz -C $MAVEN_HOME \--strip-components=1 \  
&& rm -rf maven.tar.gz*  
  
#============================  
# NodeJS  
#============================  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash - \  
&& apt-get install --yes nodejs  
  
#============================  
# Amazon AWS CLI  
#============================  
RUN curl -SL "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o awscli-
bundle.zip \  
&& unzip awscli-bundle.zip \  
&& ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws \  
&& rm -rf awscli-bundle*  
  
#============================  
# PhantomJS  
#============================  
RUN apt-get install -y libfreetype6-dev libfontconfig1-dev  
RUN wget --no-check-certificate
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-
linux-x86_64.tar.bz2 \  
&& tar -xf phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 \  
&& mv phantomjs-$PHANTOMJS_VERSION-linux-x86_64/bin/phantomjs /usr/local/bin/
\  
&& rm -rf phantom*  
  
USER jenkins  

