FROM ubuntu:14.04  
RUN dpkg --add-architecture i386 \  
&& apt-get update \  
&& apt-get install -y xinetd curl libc6:i386 libncurses5:i386 libstdc++5:i386
\  
&& curl -SL "https://downloads.sourceforge.net/project/firebird/firebird-
linux-i386/1.5.6-Release/FirebirdSS-1.5.6.5026-0.i686.tar.gz?r=&ts=1507126869&use_mirror=netcologne"
-o firebird.tar.gz \  
&& mkdir -p /usr/src/firebird \  
&& tar -xvf firebird.tar.gz -C /usr/src/firebird --strip-components=1 \  
&& rm firebird.tar.gz \  
&& cd /usr/src/firebird \  
&& printf '\nmasterkey\n' | ./install.sh \  
&& echo "PATH=$PATH:/opt/firebird/bin" >> /etc/profile \  
&& chmod +x /etc/init.d/firebird  
  
EXPOSE 3050/tcp  
ADD docker-entrypoint.sh /docker-entrypoint.sh  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT /docker-entrypoint.sh  
  

