#  
# Decred Daemon (dcrd) Docker File  
#  
# Pull base image.  
FROM centos:latest  
MAINTAINER "Reiuiji" <reiuiji@gmail.com>  
  
ENV VERSION=v1.0.3  
ENV FILE=decred-linux-amd64-$VERSION.tar.gz  
  
ENV DCRURL=https://github.com/decred/decred-
binaries/releases/download/${VERSION}/${FILE}  
  
ENV DCRDIR=/root/.dcrd  
  
# Create DCR Directory  
RUN mkdir -p ${DCRDIR}  
  
# Grab the dcrd.conf and put it in the image  
COPY dcrd.conf ${DCRDIR}/dcrd.conf  
  
#Download and extract the needed binary (dcrd)  
RUN curl -L ${DCRURL} | tar zxvf - --strip-components=1 -C /usr/bin/.  
  
#Setup Data Volume for the decred daemon  
VOLUME ${DCRDIR}  
  
#Run decred daemon on start  
CMD dcrd  
  
# Default Decred peer-to-peer port  
EXPOSE 9108  
# Default RPC port  
EXPOSE 9109  

