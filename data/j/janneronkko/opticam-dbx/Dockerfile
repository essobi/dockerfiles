FROM python:3.6-alpine3.7  
MAINTAINER Janne Rönkkö <jroo@iki.fi>  
  
RUN \  
apk add --update \  
alpine-conf \  
bash \  
ca-certificates \  
shadow \  
tzdata  
  
RUN \  
adduser -D -h /home/opticam-dbx opticam-dbx && \  
mkdir /videos && \  
chown opticam-dbx:opticam-dbx /videos  
  
COPY entrypoint /entrypoint  
RUN chmod a+rx /entrypoint  
  
ENV VIDEO_ROOT_DIR=/videos  
  
ARG OPTICAM_DBX_VERSION=0.1  
RUN pip install opticam_dbx==${OPTICAM_DBX_VERSION}  
  
ENTRYPOINT ["/entrypoint"]  

