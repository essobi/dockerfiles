# version 1.4-1  
# docker-version 0.9.1  
FROM phusion/baseimage:0.9.13  
MAINTAINER guruvan "guruvan@shastafareye.net"  
# We use a bootstrap script to avoid having temporary cache files and build  
# dependencies being committed and included into the docker image.  
VOLUME ["/home/maza"]  
ADD IMPORT /tmp/  
RUN chmod +x /tmp/bootstrap.sh ; /tmp/bootstrap.sh  
  
# p2pool peer port  
# worker & web port  
# mazacoind p2p  
EXPOSE 14476 14477 13376 13377 80 443 22  
# we leave mazacoind rpcport unexposed by default  
#ENTRYPOINT [""]  
CMD ["/sbin/my_init"]  

