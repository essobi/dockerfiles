  
FROM openjdk:8-jre-slim  
MAINTAINER Nick Ebbutt nick@chorus-bdd.org  
  
RUN apt-get update && apt-get install -y wget  
  
ENV DOCKERIZE_VERSION v0.6.0  
RUN wget
https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-
linux-amd64-$DOCKERIZE_VERSION.tar.gz \  
&& tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz
\  
&& rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz  
  
ENV CHORUS_VERSION 3.0.0  
RUN mkdir /usr/share/chorus  
RUN wget https://github.com/Chorus-
bdd/Chorus/releases/download/$CHORUS_VERSION/chorus-$CHORUS_VERSION.tar \  
&& tar -C /usr/share/chorus --strip-components=1 -xvf
chorus-$CHORUS_VERSION.tar \  
&& rm chorus-$CHORUS_VERSION.tar  
  
WORKDIR /srv/  
  
EXPOSE 9080  
ENV PATH="/usr/share/chorus:${PATH}"  
CMD ["sleep", "infinity"]  
  

