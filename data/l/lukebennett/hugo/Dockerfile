FROM phusion/baseimage  
MAINTAINER Luke Bennett <luke@lukebennett.com>  
  
# Configure working directory  
RUN mkdir /var/www  
WORKDIR /var/www  
  
# Set env vars  
ENV HUGO_VERSION 0.15  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_linux_amd64  
  
# Install pygments - provides syntax highlighting  
RUN apt-get -yq update \  
&& apt-get -yq install python-pygments \  
&& rm -rf /var/lib/apt/lists/*  
  
# Download and install hugo  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}.tar.gz
/usr/local/  
RUN tar xzf /usr/local/${HUGO_BINARY}.tar.gz -C /usr/local/ \  
&& ln -s /usr/local/${HUGO_BINARY}/${HUGO_BINARY} /usr/local/bin/hugo \  
&& rm /usr/local/${HUGO_BINARY}.tar.gz  
  
# Expose default port for use with hugo server  
EXPOSE 1313  
# Use the hugo executable by default  
ENTRYPOINT ["hugo"]

