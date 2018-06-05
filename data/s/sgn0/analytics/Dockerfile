FROM sgn0/uwsgi  
MAINTAINER Richard (Teddy) Georgeoff richard@sgn.com  
  
# runit  
RUN set -ex; \  
apk --no-cache -qXhttp://dl-cdn.alpinelinux.org/alpine/edge/community add
runit  
  
# App  
WORKDIR /var/www/app  
COPY app/requirements.txt .  
RUN set -ex; \  
apk --no-cache -q add py-pip; \  
pip install -qr requirements.txt; \  
find /usr/lib/python2.7 -name '*.py[co]' -print0 | xargs -0 rm; \  
rm -fr /root/.cache  
COPY app .  

