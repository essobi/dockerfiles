# Pull base image  
FROM alpine:3.6  
# Set build arguments  
ARG S6_OVERLAY_VERSION="v1.20.0.0"  
# Install s6-overlay  
RUN apk --no-cache add libressl \  
&& wget -qO - https://github.com/just-
containers/s6-overlay/releases/download/${S6_OVERLAY_VERSION}/s6-overlay-
amd64.tar.gz | tar zxf - -C / \  
&& apk --no-cache del libressl  
  
# Add Files  
COPY rootfs /  
  
# Define entrypoint  
ENTRYPOINT ["/init"]  
  
# Define default command  
CMD ["/bin/ash"]  

