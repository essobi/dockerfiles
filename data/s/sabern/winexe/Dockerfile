FROM debian:jessie  
  
  
  
RUN test -z "${HTTP_PROXY}" && true || echo Acquire::HTTP::Proxy
\"${HTTP_PROXY}\"\;>>/etc/apt/apt.conf.d/cache.conf  
RUN cd / && \  
apt-get update && \  
apt-get install -y git python2.7 gcc-mingw-w64 libtevent-dev samba-dev samba-
libs build-essential && \  
git clone git://git.code.sf.net/p/winexe/winexe-waf /root/winexe-winexe-waf &&
\  
cd /root/winexe-winexe-waf/source && ./waf configure build && cp /root/winexe-
winexe-waf/source/build/winexe /usr/bin/winexe && \  
apt-get -yq purge git gcc-mingw-w64 libtevent-dev samba-dev build-essential &&
apt-get -yq --purge autoremove && \  
( rm /etc/apt/apt.conf.d/cache.conf || true ) && rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /usr/local/bin/  
RUN ln -s usr/local/bin/entrypoint.sh /entrypoint.sh  
ENTRYPOINT ["entrypoint.sh"]  
CMD ["winexe"]

