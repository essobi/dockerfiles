FROM alpine:latest  
MAINTAINER Martin Peters  
  
ARG USER=ncsync  
ARG USER_UID=1000  
ARG USER_GID=1000  
  
ENV USER=$USER \  
USER_UID=$USER_UID \  
USER_GID=$USER_GID \  
NC_USER=username \  
NC_PASS=password \  
NC_URL="" \  
NC_TRUST_CERT=false \  
NC_SOURCE_DIR="/media/nextcloud/" \  
NC_SILENT=false  
# create group and user  
RUN addgroup -g $USER_GID $USER && adduser -G $USER -D -u $USER_UID $USER  
# update repositories and install nextcloud-client  
RUN apk update && apk add nextcloud-client  
  
# add run script  
ADD run.sh /usr/bin/run.sh  
  
CMD /usr/bin/run.sh  

