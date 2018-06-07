FROM linuxserver/jackett  
MAINTAINER supmagc  
  
# set version label  
ARG BUILD_DATE  
ARG VERSION  
LABEL build_version="supmagc Jackett version:- ${VERSION} Build-date:-
${BUILD_DATE}"  
  
# Configure SSL  
RUN \  
curl -sS https://curl.haxx.se/ca/cacert.pem | cert-sync --user /dev/stdin  

