FROM debian:jessie  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
build-essential libsqlite3-dev nginx libltdl-dev libyajl-dev \  
libcurl4-openssl-dev libfcgi-dev libssl-dev pkg-config \  
file net-tools \  
git openssl ca-certificates vim-tiny && \  
apt-get clean  
  
COPY sx/ /usr/local/src/sx  
RUN cd /usr/local/src/sx && \  
./configure --disable-sxhttpd --prefix /usr --sysconfdir /var/lib/sxserver/etc
--localstatedir /var && \  
make -j 3 && \  
make install  
ADD add_user.sh /root/  
RUN cp -a /var/lib/sxserver/etc/sxserver /usr/local/etc/sxserver && ln -s
/var/lib/sxserver/etc/sxserver /etc/sxserver  
RUN sed -i -e '4i[ -f /var/lib/sxserver/etc/sxserver/sxsetup.conf ] || (mkdir
-p /var/lib/sxserver/etc/sxserver && cp -a /usr/local/etc/sxserver/.
/var/lib/sxserver/etc/sxserver/.)\' /usr/sbin/sxsetup  
  
EXPOSE 80 443 8008 8443  
COPY run.sh /  
CMD ["/run.sh"]  
  

