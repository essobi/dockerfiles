FROM alpine:3.7  
LABEL maintainer "Alex Haydock <alex@alexhaydock.co.uk>"  
# Tell Go to install packages into an area that's in our default $PATH  
ENV GOPATH /usr/local  
  
# Add startup script for OnionScan  
ADD start.sh /opt/start.sh  
  
RUN set -xe \  
\  
# Install package dependencies  
&& apk update \  
&& apk add build-base git go tor \  
\  
# Install Go dependencies  
&& go get github.com/HouzuoGuo/tiedot \  
&& go get golang.org/x/crypto/openpgp \  
&& go get golang.org/x/net/proxy \  
&& go get golang.org/x/net/html \  
&& go get github.com/rwcarlsen/goexif/exif \  
&& go get github.com/rwcarlsen/goexif/tiff \  
\  
# Install OnionScan  
&& go get github.com/s-rah/onionscan \  
\  
# Configure Tor to run in the background  
&& echo "RunAsDaemon 1" > /etc/tor/torrc \  
\  
# Make startup script executable  
&& chmod +x /opt/start.sh \  
\  
# Create a directory for us to execute OnionScan inside  
&& mkdir /opt/onionscan \  
&& chown -R tor /opt/onionscan  
  
# Set our workdir and run as the 'tor' user so we can launch the Tor binary  
WORKDIR /opt/onionscan  
USER tor  
  
# Run  
# (This script passes arguments given to the Docker command straight to the
OnionScan binary. If no argument  
# is given then the CMD will apply and OnionScan will run a scan of the
DuckDuckGo hidden service).  
ENTRYPOINT ["/opt/start.sh"]  
CMD ["3g2upl4pq6kufc4m.onion"]  

