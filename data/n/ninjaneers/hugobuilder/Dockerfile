FROM ubuntu:xenial  
MAINTAINER cgd@ninjaneers.de  
  
# Download and install hugo  
ENV HUGO_VERSION 0.16  
ENV HUGO_BINARY hugo_${HUGO_VERSION}-1_amd64.deb  
  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}
/tmp/hugo.deb  
RUN dpkg -i /tmp/hugo.deb \  
&& rm /tmp/hugo.deb  
  
RUN mkdir /source  
RUN mkdir /target  
  
WORKDIR /source  
VOLUME /source /target  
  
ENTRYPOINT ["/usr/bin/hugo", "-d", "/target"]  
CMD ["--cleanDestinationDir"]

