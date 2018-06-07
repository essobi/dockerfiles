FROM l3iggs/archlinux:latest  
MAINTAINER Nathan Hourt<nathan@bitshares.org>  
  
ADD bitshares_loop /  
ENTRYPOINT /bitshares_loop  
  
COPY config.json /root/.BitShares/config.json  
COPY node_config.json /root/.BitShares/node_config.json  
  
EXPOSE 1375 1376 1377 1776  
WORKDIR /tmp  
ADD bootstrap /tmp/  
ADD bitshares-cli.src.tar.xz /tmp/  
  
RUN ./bootstrap  
RUN bitshares-cli --statistics-enabled --rebuild-index  

