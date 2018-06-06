FROM debian:jessie  
  
RUN apt-get update && \  
apt-get install -y wget && \  
rm -r /var/lib/apt/lists/*  
  
ENV NODE_VERSION 4.2.4  
RUN wget http://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz  
RUN mkdir /nodejs \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /nodejs --strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz"  
  
ENV PATH $PATH:/nodejs/bin  
  
# Install SSL cert of 104  
#COPY ./cert/*.crt /usr/local/share/ca-certificates/  
#RUN chmod 640 /usr/local/share/ca-certificates/* && update-ca-certificates  
ENV JENKINS_HOME /var/jenkins_home  
RUN useradd -d "$JENKINS_HOME" -u 1000 -m -s /bin/bash jenkins  
#VOLUME /var/jenkins_home  
RUN mkdir /app && chown jenkins:jenkins /app  
  
WORKDIR /app  
USER jenkins  
CMD ['npm start']  

