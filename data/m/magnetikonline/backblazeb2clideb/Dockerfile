FROM ubuntu:16.04  
MAINTAINER Peter Mescalchin <peter@magnetikonline.com>  
  
ENV VERSION 0.7.2  
RUN apt-get update && apt-get -y upgrade && \  
apt-get -y install checkinstall python python-pip && \  
apt-get clean  
  
ADD https://github.com/Backblaze/B2_Command_Line_Tool/archive/v$VERSION.tar.gz
/root/build/  
  
WORKDIR /root/build  
RUN tar -xf v$VERSION.tar.gz  
  
WORKDIR /root/build/B2_Command_Line_Tool-$VERSION  
RUN echo "magnetikonline: Backblaze B2 CLI" >description-pak && \  
checkinstall -Dy --install=no --nodoc --pkgname=backblaze-cli
--pkgversion=$VERSION python setup.py install  
  
CMD ["/bin/bash"]  

