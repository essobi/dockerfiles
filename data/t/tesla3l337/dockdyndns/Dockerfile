# sshd  
#  
# VERSION 0.0.2  
  
FROM alpine:edge  
MAINTAINER Tesla <tesla@v-ip.fr>  
  
  
  
  
ENV API_USER "root"  
ENV API_PWD "root"  
  
COPY ./djbdns-fwdzone.patch /  
  
RUN adduser seed -u 666 -g 666 -D && apk add \--update \--virtual build-deps
build-base python-dev && \  
apk add python curl wget make bind-tools apache2-utils && \  
wget https://cr.yp.to/djbdns/djbdns-1.05.tar.gz && \  
tar xvfz djbdns-1.05.tar.gz && \  
echo gcc -O2 -include /usr/include/errno.h > djbdns-1.05/conf-cc && \  
cd djbdns-1.05 && \  
patch -p1 < /djbdns-fwdzone.patch && \  
make -j 4 setup check && cd .. && \  
rm -rf /djbdns-1.05 && rm djbdns-1.05.tar.gz && rm /djbdns-fwdzone.patch && \  
wget http://cr.yp.to/daemontools/daemontools-0.76.tar.gz && \  
tar xvfz daemontools-0.76.tar.gz && \  
echo gcc -O2 -include /usr/include/errno.h > admin/daemontools-0.76/src/conf-
cc && \  
cd admin/daemontools-0.76/ && sh package/install && \  
rm /daemontools-0.76.tar.gz && \  
curl -sS https://bootstrap.pypa.io/get-pip.py | python && \  
pip install docker-py && \  
apk del build-deps && \  
adduser -S svclog && adduser -S dnscache && adduser -S tinydns && \  
dnscache-conf dnscache svclog /etc/dnscache && \  
tinydns-conf tinydns svclog /etc/tinydns 0.0.0.0 && \  
ln -s /etc/dnscache /service/dnscache && ln -s /etc/tinydns /service/tinydns
&& ln -s /service/ /etc/service && \  
touch /etc/dnscache/root/ip/172 && \  
echo "#!/bin/sh" > /etc/dnscache/log/run && \  
echo "exec setuidgid svclog multilog t '-*' '+* fatal: *' ./main" >>
/etc/dnscache/log/run && \  
echo "127.0.0.1">/etc/dnscache/root/servers/docker && echo
"127.0.0.1">/etc/dnscache/root/servers/0.17.172.in-addr.arpa  
  
  
  
COPY ./event.py /  
  
COPY ./docker-entrypoint.sh /  
COPY ./tinydnsdyn /usr/bin/  
  
EXPOSE 53:53  
ENTRYPOINT ["/docker-entrypoint.sh"]  

