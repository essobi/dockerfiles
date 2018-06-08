FROM alpine:latest  
MAINTAINER "Nick Thieling" <nick@adrift.io>  
  
ENV VERSION=v1.2.0  
ENV FILE=decred-linux-amd64-$VERSION.tar.gz  
ENV DCR_DIST_URL=https://github.com/decred/decred-
binaries/releases/download/${VERSION}/${FILE}  
ENV DCR_DATA_DIR=/root/.dcrd  
ENV DCR_RPC_USER=user  
ENV DCR_RPC_PASS=pass  
  
VOLUME ${DCR_DATA_DIR}  
EXPOSE 9108 9109  
# prerequisites  
RUN apk add --no-cache curl tar  
  
# Create DCR Directory  
RUN mkdir -p ${DCR_DATA_DIR}  
  
# Grab the dcrd.conf and put it in the image  
COPY dcrd.conf ${DCR_DATA_DIR}/dcrd.conf  
  
#Download and extract the needed binary (dcrd)  
RUN curl -L ${DCR_DIST_URL} | tar zxvf - --strip-components=1 -C /usr/bin/.  
  
#Run decred daemon on start  
ENTRYPOINT [ "dcrd -u ${DCR_RPC_USER} -P ${DCR_RPC_PASS} \--notls --txindex
--listen=" ]  

