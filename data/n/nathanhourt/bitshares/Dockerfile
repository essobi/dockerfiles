FROM l3iggs/archlinux:latest  
MAINTAINER Nathan Hourt<nathan@bitshares.org>  
  
ADD bitshares_loop /  
ENTRYPOINT /bitshares_loop  
  
WORKDIR /tmp  
ADD bootstrap /tmp/  
ADD bitshares-cli.src.tar.xz /tmp/  
  
RUN ./bootstrap  
RUN bitshares-cli  

