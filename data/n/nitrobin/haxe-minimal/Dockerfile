FROM debian:jessie  
MAINTAINER nitrobin  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Dependencies  
RUN apt-get update \  
&& apt-get install -y \  
wget \  
libgc-dev \  
&& apt-get clean  
  
################################################################################  
  
# Neko environment variables  
ENV NEKOVERSION=2.0.0 NEKOPATH=/opt/neko  
  
# Download Neko  
RUN mkdir -p $NEKOPATH && \  
wget -O - http://nekovm.org/_media/neko-$NEKOVERSION-linux64.tar.gz \  
| tar xzf - --strip=1 -C $NEKOPATH  
ENV LD_LIBRARY_PATH $NEKOPATH  
ENV PATH $NEKOPATH:$PATH  
  
################################################################################  
  
# Haxe environment variables  
ENV HAXEVERSION=3.2.1 HAXEPATH=/opt/haxe HAXELIB_PATH=/opt/haxelib  
  
# Download Haxe  
RUN mkdir -p $HAXEPATH && \  
wget -O - http://haxe.org/website-
content/downloads/$HAXEVERSION/downloads/haxe-$HAXEVERSION-linux64.tar.gz \  
| tar xzf - --strip=1 -C $HAXEPATH && \  
mkdir -p $HAXELIB_PATH && echo $HAXELIB_PATH > /root/.haxelib && cp
/root/.haxelib /etc/  
ENV HAXE_STD_PATH $HAXEPATH/std/  
ENV PATH $HAXEPATH:$PATH  
  
# workaround for https://github.com/HaxeFoundation/haxe/issues/3912  
ENV HAXE_STD_PATH $HAXE_STD_PATH:.:/  
  
################################################################################  
  
ADD test /root/test  
RUN /root/test/verify.sh  
  
ADD home/install-nightly-haxe.sh /root/  
#RUN /root/install-nightly-haxe.sh  
  
CMD ["/bin/bash"]  

