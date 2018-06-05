FROM ubuntu:15.10  
MAINTAINER "Michele Bariani" <michele.bariani@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update ; apt-get -y install vim curl build-essential csh man-db ;
apt-get clean all  
  
ADD . /root  
  
WORKDIR /root  
RUN curl http://www.rulequest.com/Personal/c4.5r8.tar.gz | tar xz ;\  
chmod -R u+w R8 ;\  
patch -u -p0 -i c4.5.patch ;\  
mv R8/Data /root/example_data ;\  
mv R8/Doc/* /usr/share/man/man1/ ;\  
cd R8/Src ;\  
make all ;\  
mv c4.5 c4.5rules consult consultr xval-prep average xval.sh /usr/local/bin ;\  
cd ../.. ;\  
rm -fr R8 c4.5.patch  
  
RUN mkdir c5.0 ;\  
cd c5.0 ;\  
curl http://rulequest.com/GPL/C50.tgz | tar xz ;\  
make all ;\  
mv c5.0 report xval /usr/local/bin/ ;\  
cd .. ;\  
rm -fr c5.0  
  

