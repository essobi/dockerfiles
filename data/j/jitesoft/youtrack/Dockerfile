FROM openjdk:8-jre-alpine  
LABEL maintainer="Johannes Tegnér <johannes@jitesoft.com>"  
  
ENV YOUTRACK_VERSION=2018.1.41561  
EXPOSE 8080  
# Using the zip installation for the ability to use an external hub if wanted.  
RUN apk add --no-cache --virtual .trash wget unzip && \  
wget https://download.jetbrains.com/charisma/youtrack-$YOUTRACK_VERSION.zip -O
youtrack.zip && \  
unzip youtrack.zip && \  
rm youtrack.zip && \  
mv youtrack-* youtrack && \  
apk del .trash  
  
CMD ["/bin/ash", "-c", "youtrack/bin/youtrack.sh run"]  

