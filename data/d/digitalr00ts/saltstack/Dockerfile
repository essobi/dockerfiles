FROM digitalr00ts/saltstack-base:latest  
  
LABEL maintainer="Carlos@digitalr00ts.com"  
ARG SALT_VER=latest  
  
HEALTHCHECK \--interval=1m \--timeout=3s \--start-period=20s \--retries=3 \  
CMD nc -zw 1 localhost 4505 && nc -zw 1 localhost 4506 && test-api || exit 1  
  
EXPOSE 4505 4506  
  
VOLUME ['/srv/etc/salt/pki/']  
  
RUN cd && set -ex && \  
apk add \--update \--virtual .build-dependencies curl gcc musl-dev libffi-dev
libressl-dev python2-dev zeromq-dev curl-dev libssh2-dev && \  
apk add py-mysqldb libgit2 libssh2 libpthread-stubs ca-certificates && \  
curl -SsLO https://bootstrap.pypa.io/get-pip.py && \  
curl -SsLO https://github.com/digitalr00ts/docker-
saltstack/raw/develop/_files/requirements.txt && \  
curl -SsLO https://github.com/digitalr00ts/docker-
saltstack/raw/develop/_config/master && \  
mv master /etc/salt/ && \  
curl -SsLO https://github.com/digitalr00ts/docker-
saltstack/raw/develop/_files/start-salt.sh && \  
chmod +x start-salt.sh && mv start-salt.sh /usr/local/bin/start-salt && \  
curl -SsLO https://github.com/digitalr00ts/docker-
saltstack/raw/develop/_files/test-api.py && \  
chmod +x test-api.py && mv test-api.py /usr/local/bin/test-api && \  
touch /srv/etc/salt/roster && \  
python get-pip.py && rm -f get-pip.py && \  
pip \--no-cache-dir install salt$([ "$SALT_VER" = 'latest' ] || echo
"==${SALT_VER}") && \  
pip \--no-cache-dir install -r requirements.txt && \  
rm -f /root/requirements.txt && \  
pip list \--format=columns > /root/pip-list.txt && \  
python -m pip uninstall \--yes pip && \  
apk del .build-dependencies ;\  
rm -rf \-- /var/cache/apk/* /var/lib/apk/* /etc/apk/cache/* /root/.cache  
  
CMD ["/usr/local/bin/start-salt"]  

