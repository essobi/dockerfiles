FROM debian:jessie  
  
MAINTAINER Deon Thomas "deon.thomas.gy@gmail.com"  
ENV HHVM_VERSION 3.21.10-1~jessie  
  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0xB4112585D386EB94 \  
&& echo 'deb http://dl.hhvm.com/debian jessie-lts-3.21 main' >
/etc/apt/sources.list.d/hhvm.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
ca-certificates \  
hhvm=$HHVM_VERSION \  
&& /usr/bin/update-alternatives --install /usr/bin/php php /usr/bin/hhvm 60 \  
&& rm -rf /var/lib/apt/lists/*  
  
EXPOSE 9000  
COPY entrypoint.sh /  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["hhvm", "-m", "server", "-vServer.Type=fastcgi", "-vServer.Port=9000",
"-vServer.AllowRunAsRoot=1"]  

