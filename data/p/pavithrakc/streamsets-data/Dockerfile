FROM alpine:3.4  
MAINTAINER Pavithra K C <Pavithra.KC@intlfcstone.com>  
  
#ARG
SDC_URL=https://archives.streamsets.com/datacollector/2.4.1.0/tarball/streamsets-
datacollector-core-2.4.1.0.tgz  
ARG SDC_USER=sdc  
  
USER root  
  
  
RUN apk --no-cache add bash \  
curl \  
krb5-libs \  
libstdc++ \  
sed  
  
RUN mkdir /opt  
  
  
# add streamsets user  
RUN addgroup -S ${SDC_USER} && \  
adduser -S ${SDC_USER} ${SDC_USER}  
  
  
ARG DATA_VOLUME=/usr/share/streamsets/data  
  
RUN mkdir -p ${DATA_VOLUME}  
# Set permissions on shared libs folder  
RUN chown -R "${SDC_USER}:${SDC_USER}" "${DATA_VOLUME}"  
  
  
ENTRYPOINT ["/bin/true"]  
  
  
  

