FROM scratch  
MAINTAINER John Regan <john@jrjrtech.com>  
ADD rootfs.tar /  
  
USER default  
  
ENV HOME /home/default  
WORKDIR /home/default  
ADD hello.lol /home/default/hello.lol  
  
ENTRYPOINT ["lci"]  
CMD ["hello.lol"]  

