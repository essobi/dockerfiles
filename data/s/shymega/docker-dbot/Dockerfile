################################  
# Dockerfile for depressionbot #  
################################  
  
# Set base image  
FROM alpine:3.4  
  
# Set maintainer.  
MAINTAINER shymega <shymega@shymega.org.uk>  
  
# Node.js install.  
# Update packages and install.  
RUN apk add --update nodejs redis git wget unzip bash  
  
# Create docker container user.  
ENV USERNAME docker  
RUN addgroup -S "$USERNAME" \  
&& adduser -S "$USERNAME" -h /docker \  
&& adduser "$USERNAME" "$USERNAME"  
  
# Set user for the installation  
USER "$USERNAME"  
  
# Clone dbot into /docker/dbot  
RUN git clone https://github.com/reality/dbot.git /docker/dbot  
  
# Install dbot using the provided script.  
WORKDIR /docker/dbot  
RUN EDITOR=/bin/true /docker/dbot/install  
  
# Set user back to root to cleanup  
USER root  
RUN apk del --no-cache --rdepends git py-pip g++ make  
  
# Set user back to docker use for runtime execution  
USER "$USERNAME"  
  
# Set runtime command.  
CMD ["node", "/docker/dbot/run.js"]  

