FROM centos:7  
LABEL maintainer Parker Johansen <johansen.parker@gmail.com>  
  
ARG setupdir=/factoriosetup  
ARG factorioversion=0.14.22  
RUN yum update -y && \  
yum install -y wget  
  
RUN mkdir $setupdir && \  
cd $setupdir && \  
wget https://www.factorio.com/get-download/$factorioversion/headless/linux64
-O factorio-headless.tar.gz && \  
tar -xzf factorio-headless.tar.gz && \  
mkdir factorio/settings && \  
mv factorio /factorio && \  
rm -rv $setupdir  
  
COPY serversettings.py startfactorio.sh /factorio/  
  
RUN chmod +x /factorio/startfactorio.sh  
  
ENV ADMIN="" GAMEPASS=""  
VOLUME /factorio/saves /factorio/mods /factorio/settings  
  
EXPOSE 34197/udp  
  
CMD /factorio/startfactorio.sh $ADMIN $GAMEPASS  

