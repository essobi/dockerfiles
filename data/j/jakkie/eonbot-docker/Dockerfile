FROM ubuntu:latest  
  
RUN apt-get update && apt-get install -y wget && apt-get clean  
  
ARG EONBOT_VERSION=1.4.1  
ENV EONBOT_VERSION ${EONBOT_VERSION}  
  
RUN mkdir -p /eonbot/subconfigs  
WORKDIR /eonbot  
  
RUN wget -O eonbot
https://www.dropbox.com/sh/3oa4l6gkdmg20jq/AACletJk4po_BSGby491t2h0a/v$EONBOT_VERSION/eonbot-v$EONBOT_VERSION-
linux-amd64?dl=1  
RUN ls -a  
RUN chmod +x eonbot  
  
VOLUME /eonbot/  
  
CMD ./eonbot  
  
EXPOSE 9999  

