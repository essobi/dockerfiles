FROM debian:wheezy  
MAINTAINER PRESYSTEMS Inc.  
RUN apt-get update && apt-get install -y git libglib2.0-dev gcc make  
  
WORKDIR /root  
RUN git clone https://github.com/nagatou/rccs  
RUN cd rccs/src \  
&& mkdir -p /usr/lib/glib-2.0 && ln -s `pkg-config --cflags glib-2.0 | awk
'{print substr($2,3)}'` /usr/lib/glib-2.0 \  
&& make rccs \  
&& cp rccs /usr/local/bin  

