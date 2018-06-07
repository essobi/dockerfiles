FROM ubuntu:rolling  
  
## I need to install python3, golang+hugo & node/npm(recentish) here  
RUN apt-get update  
RUN apt-get install -y apt-utils build-essential git curl  
  
# Install Python.  
RUN apt-get install -y python3.6 python3.6-dev python3-pip python3-virtualenv
&& \  
rm -rf /var/lib/apt/lists/*  
  
# Download and install hugo  
ENV HUGO_VERSION 0.27.1  
ENV HUGO_BINARY hugo_${HUGO_VERSION}_Linux-64bit.deb  
ADD
https://github.com/spf13/hugo/releases/download/v${HUGO_VERSION}/${HUGO_BINARY}
/tmp/hugo.deb  
RUN dpkg -i /tmp/hugo.deb \  
&& rm /tmp/hugo.deb  
  
# Download and install Node 8. Also installs npm  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
  
# Endpointer  
RUN pip3 install endpointer  
  
WORKDIR /build  
  
ADD . /build  
  
#ADD ./dist /build/public  
ENTRYPOINT ["/bin/sh", "-c"]  

