#------------------------------------------------------------------------------  
# Set the base image for subsequent instructions:  
#------------------------------------------------------------------------------  
FROM alpine:3.3  
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>  
  
#------------------------------------------------------------------------------  
# Environment variables:  
#------------------------------------------------------------------------------  
ENV MDNS_VERSION="0.5.2" \  
MDNS_URL="https://github.com/mesosphere/mesos-dns/releases/download"  
#------------------------------------------------------------------------------  
# Install Mesos DNS and KViator  
#------------------------------------------------------------------------------  
RUN apk --no-cache add --update -t deps openssl unzip ca-certificates \  
&& apk --no-cache add --update bash curl \  
&& wget ${MDNS_URL}/v${MDNS_VERSION}/mesos-dns-v${MDNS_VERSION}-linux-amd64 -O
/bin/mesos-dns \  
&& chmod +x /bin/mesos-dns \  
&& apk del --purge deps \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
#------------------------------------------------------------------------------  
# Populate root file system:  
#------------------------------------------------------------------------------  
ADD rootfs /  
  
#------------------------------------------------------------------------------  
# Expose ports and entrypoint:  
#------------------------------------------------------------------------------  
EXPOSE 53  
ENTRYPOINT ["/init"]  

