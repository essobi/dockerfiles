FROM java:8-jdk  
MAINTAINER Evan Lowry <evan@pitchplay.io>  
  
WORKDIR /usr/bin  
  
# Install SBT  
RUN wget https://raw.githubusercontent.com/paulp/sbt-extras/master/sbt \  
&& chmod +x sbt  
  
WORKDIR /tmp  
RUN /usr/bin/sbt -sbt-create -211  
  
# Install Node  
ENV NODE_VERSION 0.12.5  
ENV NPM_VERSION 2.11.3  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  
# Install graphviz  
RUN apt-get update && apt-get install -y graphviz  
  
# Dummy placeholder  
CMD ["/usr/bin/sbt", "-h"]  

