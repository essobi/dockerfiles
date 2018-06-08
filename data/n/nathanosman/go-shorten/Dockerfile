FROM alpine  
MAINTAINER Nathan Osman <nathan@quickmediasolutions.com>  
  
# Add the binary  
ADD dist/go-shorten /usr/local/bin/  
  
# Create the default configuration file  
RUN \  
mkdir -p /etc/go-shorten && \  
cd /etc/go-shorten && \  
go-shorten  
  
# Expose the HTTP port  
EXPOSE 80  
# Specify the entrypoint  
ENTRYPOINT ["/usr/local/bin/go-shorten", "/etc/go-shorten/config.json"]  

