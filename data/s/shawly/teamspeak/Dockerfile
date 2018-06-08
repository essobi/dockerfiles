#  
# teamspeak Dockerfile  
#  
# https://github.com/shawly/docker-teamspeak  
#  
# Pull base image.  
FROM jlesage/baseimage:alpine-3.7-glibc  
  
# Define working directory.  
WORKDIR /tmp  
  
# Install teamspeak.  
ADD teamspeak-builder/teamspeak.tar.gz /  
  
# Install ca certificates.  
RUN apk --no-cache add ca-certificates  
  
# Add files.  
COPY rootfs/ /  
  
# Set environment variables.  
ENV APP_NAME="teamspeak" \  
TS3SERVER_LICENSE="accept" \  
TAKE_CONFIG_OWNERSHIP="1"  
# Define mountable directories.  
VOLUME ["/config"]  
  
# Expose ports.  
EXPOSE 9987/udp 30033 10011 2010/udp 41144 2008  
# Metadata.  
LABEL \  
org.label-schema.name="teamspeak" \  
org.label-schema.description="Docker container for teamspeak" \  
org.label-schema.version="unknown" \  
org.label-schema.vcs-url="https://github.com/shawly/docker-teamspeak" \  
org.label-schema.schema-version="1.0"  

