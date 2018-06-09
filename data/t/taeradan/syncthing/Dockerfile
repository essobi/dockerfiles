FROM debian  
MAINTAINER Yves Dubromelle <yves+docker@dubronetwork.fr>  
  
ENV VERSION v0.12.3  
ENV RELEASE syncthing-linux-amd64-$VERSION  
  
ADD
https://github.com/syncthing/syncthing/releases/download/$VERSION/$RELEASE.tar.gz
/$RELEASE.tar.gz  
  
RUN gzip -d /$RELEASE.tar.gz && \  
tar -xf /$RELEASE.tar && \  
rm /$RELEASE.tar* && \  
mv /$RELEASE /syncthing  
  
RUN useradd --create-home syncthing  
  
EXPOSE 8080 22000 21025/udp  
  
USER syncthing  
  
CMD ["/syncthing/syncthing"]  

