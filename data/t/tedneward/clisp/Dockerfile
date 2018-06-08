FROM ubuntu  
MAINTAINER Ted Neward <ted@tedneward.com>  
  
RUN apt-get update && \  
apt-get install -y clisp  
  
RUN groupadd --gid 1000 clisp \  
&& useradd --uid 1000 --gid clisp --shell /bin/bash --create-home clisp \  
&& chown -R clisp:clisp /usr/local  
  
USER clisp  
WORKDIR /home/clisp  
  
ENTRYPOINT ["/bin/bash"]  

