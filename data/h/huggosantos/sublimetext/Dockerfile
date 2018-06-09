FROM ubuntu:14.04  
MAINTAINER Huggo Santos Oliveira <huggo.oliveira1@gmail.com>  
  
RUN apt-get update && apt-get -y install \  
ca-certificates \  
curl \  
tar \  
bzip2 \  
libglib2.0-0 \  
libx11-6 \  
libcairo2 \  
libpango-1.0-0 \  
libpangocairo-1.0-0 \  
libgtk2.0-0 \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -q -y axel  
  
RUN axel https://download.sublimetext.com/sublime-text_build-3103_amd64.deb  
RUN dpkg -i sublime-text_build-3103_amd64.deb  
  
CMD /opt/sublime_text/sublime_text  

