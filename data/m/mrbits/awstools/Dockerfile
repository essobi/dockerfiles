FROM alpine:3.7  
LABEL "Maintainer"="MrBiTs"  
LABEL "e-mail"="mrbits.dcf@gmail.com"  
LABEL "version"="1.0.0"  
RUN \  
apk update && \  
apk add git python py-pip && \  
pip install --upgrade pip awsebcli  
  
RUN git config \--global advice.detachedHead false  

