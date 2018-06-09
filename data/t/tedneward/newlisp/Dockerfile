FROM ubuntu  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
RUN apt-get update && apt-get install -y curl  
  
RUN groupadd --gid 1000 newlisp \  
&& useradd --uid 1000 \--gid newlisp \--shell /bin/bash --create-home newlisp
\  
&& chown -R newlisp:newlisp /usr/local  
  
ENV NEWLISP_VER=10.7.1  
RUN curl -fsSL -o /tmp/newlisp_${NEWLISP_VER}.deb
http://www.newlisp.org/downloads/newlisp_${NEWLISP_VER}-utf8_amd64.deb && \  
dpkg -i /tmp/newlisp_${NEWLISP_VER}.deb  
  
USER newlisp  
WORKDIR /home/newlisp  
  
ENTRYPOINT ["/bin/bash"]  

