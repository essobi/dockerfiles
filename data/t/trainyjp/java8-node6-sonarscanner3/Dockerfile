FROM buildpack-deps:jessie  
  
ENTRYPOINT ["/bin/bash"]  
  
ENV NODE_VERSION 6.10.3  
ENV TYPESCRIPT_VERSION 2.0.10  
ENV TSLINT_VERSION 4.2.0  
ENV SONARSCANNER_FILENAME sonar-scanner-cli-3.0.3.778.zip  
ENV SONARSCANNER_DIR sonar-scanner-3.0.3.778  
# if you should set proxy for container, build with args.  
# example:  
# docker build -t docker-java8-node6 . --build-arg HTTP_PROXY=http://proxy-
host:proxy-port  
# write proxy setting  
RUN echo "http_proxy=$HTTP_PROXY" > /etc/wgetrc && \  
echo "https_proxy=$HTTP_PROXY" >> /etc/wgetrc  
RUN echo "Acquire::http::Proxy \"$HTTP_PROXY\";" > /etc/apt/apt.conf.d/02proxy
&& \  
echo "Acquire::https::Proxy \"$HTTP_PROXY\";" >> /etc/apt/apt.conf.d/02proxy
&& \  
echo "Acquire::ftp::Proxy \"$HTTP_PROXY\";" >> /etc/apt/apt.conf.d/02proxy  
  
# install zip  
RUN apt-get update && \  
apt-get -y install unzip zip  
  
# install nodejs  
RUN wget "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" && \  
tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 && \  
ln -s /usr/local/bin/node /usr/local/bin/nodejs && \  
rm "/node-v$NODE_VERSION-linux-x64.tar.xz"  
  
# write proxy setting  
RUN npm -g config set proxy $HTTP_PROXY  
  
# install typescript & tslint  
RUN npm -g config set registry http://registry.npmjs.org/ && \  
npm install -g "typescript@$TYPESCRIPT_VERSION" "tslint@$TSLINT_VERSION"  
  
# install java8  
RUN echo "deb http://ftp.jp.debian.org/debian jessie-backports main" >
/etc/apt/sources.list.d/jessie-backports.list && \  
apt-get update && \  
apt-get install -y -t jessie-backports ca-certificates-java && \  
apt-get install -y openjdk-8-jre openjdk-8-jre-headless openjdk-8-jdk
openjdk-8-jdk-headless  
  
# install maven  
RUN apt-get -y install maven  
  
# make java8 default  
RUN update-java-alternatives --set java-1.8.0-openjdk-amd64  
  
# install sonar-scanner  
RUN wget "https://sonarsource.bintray.com/Distribution/sonar-scanner-
cli/$SONARSCANNER_FILENAME" && \  
unzip "$SONARSCANNER_FILENAME" -d /opt && \  
ln -s "/opt/$SONARSCANNER_DIR/bin/sonar-scanner" /usr/local/bin/sonar-scanner
&& \  
rm "/$SONARSCANNER_FILENAME"  
  
# install git from jessie-backports  
RUN apt-get install -y -t jessie-backports git  

