FROM ubuntu:15.10  
MAINTAINER Leonardo Saraiva <vyper@maneh.org>  
  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y xinetd curl libc6:i386 libncurses5:i386 libstdc++5:i386
\  
&& curl -SL "http://downloads.sourceforge.net/project/firebird/firebird-
linux-i386/1.5.6-Release/FirebirdCS-1.5.6.5026-0.i686.tar.gz" -o
firebird.tar.gz \  
&& mkdir -p /usr/src/firebird \  
&& tar -xvf firebird.tar.gz -C /usr/src/firebird --strip-components=1 \  
&& rm firebird.tar.gz \  
&& cd /usr/src/firebird \  
&& sed -i "141s/^/# /" install.sh \  
&& sed -i "141s/^/# /" scripts/tarMainInstall.sh \  
&& sed -i "323,324s/^/# /" scripts/postinstall.sh \  
&& sed -i "324aNewPasswd=masterkey" scripts/postinstall.sh \  
&& sh install.sh \  
&& rm -rf /usr/src/firebird  
  
ENV PATH $PATH:/opt/firebird/bin  
  
CMD ["isql"]  

