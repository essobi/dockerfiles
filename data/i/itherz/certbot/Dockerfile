FROM python:2.7-alpine  
MAINTAINER James Z.M. Gao <gaozm55@gmail.com>  
  
COPY content /  
  
RUN set -ex \  
&& apk update \  
&& apk add --no-progress --virtual .letsencrypt-rundeps \  
dialog \  
augeas-libs \  
libffi wget \  
libssl1.0 \  
ca-certificates \  
binutils \  
&& apk add --no-progress --virtual .build-deps \  
gcc \  
linux-headers \  
openssl-dev \  
musl-dev \  
libffi-dev \  
&& wget -qO-
https://raw.githubusercontent.com/certbot/certbot/master/letsencrypt-auto \  
| grep -v ' rm -rf .*VENV_PATH' \  
| grep -v 'VENV_BIN/python.*pipstrap.py' \  
| sed '1avirtualenv() { :; }' \  
| sed '/Installation succeeded/aexit 0' \  
| VENV_PATH=/usr/local /bin/sh -s -- --le-auto-phase2 --no-self-upgrade \  
&& ln -s "$(find /usr/lib -type f -name libaugeas.so.* | head -1)"
/usr/lib/libaugeas.so \  
&& patch -p 0 -i /python-ctypes-issue9998.patch \  
&& apk del .build-deps \  
&& find /usr/local -depth \  
\\( \\( -type d -a -name test -o -name tests \\) \  
-o \  
\\( -type f -a -name '*.pyc' -o -name '*.pyo' \\) \  
\\) -exec rm -rf '{}' \+ \  
&& rm -rf ~/.cache /var/cache/apk/* /tmp/* /*.patch  
  
EXPOSE 80  
EXPOSE 443  
  
VOLUME /etc/letsencrypt /var/lib/letsencrypt  
  
ENTRYPOINT ["/entrypoint.sh"]  

