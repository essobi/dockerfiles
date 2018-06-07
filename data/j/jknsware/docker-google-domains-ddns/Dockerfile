FROM alpine:3.6  
LABEL \  
image_name=jknsware/docker-google-domains-ddns \  
description="Google Domains Dynamic DNS Updater" \  
maintainer="jason@jknsware.com" \  
dockerfile_location=https://github.com/jknsware/docker-google-domains-
ddns/Dockerfile \  
base_image=alpine:3.6  
  
# Set environmentals  
ENV USER_AGENT=  
ENV HOSTNAME=  
ENV USERNAME=  
ENV PASSWORD=  
ENV INTERVAL=  
  
# Install curl and bash  
RUN apk --no-cache add curl bash  
  
# Add the script, set +x, and run it  
ADD /conf /  
  
RUN chmod +x /usr/local/bin/google-domain.sh  
  
ENTRYPOINT ["/usr/local/bin/google-domain.sh"]

