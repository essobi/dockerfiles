FROM debian:jessie  
  
ENV HHVM_VERSION 3.3.7~jessie  
  
RUN apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80
0x5a16e7281be7a449 \  
&& echo 'deb http://dl.hhvm.com/debian jessie-lts-3.3 main' >
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
  
CMD ["hhvm", "-m", "server", "-vServer.Type=fastcgi", "-vServer.Port=9000"]  

