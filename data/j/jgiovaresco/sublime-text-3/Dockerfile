# VERSION: 0.1  
# DESCRIPTION: Create Sublime Text 3 container (https://www.sublimetext.com/3)  
# AUTHOR: Julien Giovaresco <dev@giovaresco.fr>  
# USAGE:  
#  
# # Run the container and mount the local settings and a directory  
# docker run -it \  
# -v /tmp/.X11-unix:/tmp/.X11-unix \  
# -e DISPLAY=$DISPLAY  
# -v $HOME/.sublime-text-3/:/root/.config/sublime-text-3 \  
# -v $HOME/DEV:/root/DEV \  
# jgiovaresco/sublime-text-3  
  
FROM jgiovaresco/debian-with-dockerize:latest  
MAINTAINER Julien Giovaresco <dev@giovaresco.fr>  
  
RUN apt-get update && apt-get -y install \  
bzip2 \  
ca-certificates \  
curl \  
git \  
libglib2.0-0 \  
libx11-6 \  
libcairo2 \  
libpango-1.0-0 \  
libpangocairo-1.0-0 \  
libgtk2.0-0 \  
tar \  
\--no-install-recommends \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sSL
"http://c758482.r82.cf2.rackcdn.com/sublime_text_3_build_3083_x64.tar.bz2" -o
/tmp/sublime.tar.bz2 \  
&& mkdir -p /opt/sublime_text \  
&& tar -xjf /tmp/sublime.tar.bz2 -C /opt/sublime_text --strip-components 1 \  
&& rm /tmp/sublime.tar.bz2*  
  
CMD ["/opt/sublime_text/sublime_text", "-w"]  

