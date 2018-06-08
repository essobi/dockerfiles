FROM sgn0/uwsgi  
MAINTAINER Jesus Lopez, jesus@sgn.com  
  
# runit  
RUN set -ex; \  
apk --no-cache -qXhttp://dl-cdn.alpinelinux.org/alpine/edge/community add
runit  
  
# From sgn0/nginx  
# nginx  
RUN set -ex; \  
apk --no-cache -q add nginx  
  
COPY .nginx/service /etc/service/  
COPY .nginx/conf /etc/nginx/  
COPY .nginx/bin /usr/sbin/  
  
RUN set -ex; \  
ln -s /usr/sbin/nginx_ensite /usr/sbin/nginx_dissite; \  
nginx_ensite default  
  
# docker  
COPY config.json /root/.docker/  
RUN set -ex; \  
apk add --no-cache -q docker; \  
apk add --no-cache -qt .deps binutils; \  
apk info -L docker git |grep / |grep -v docker$ |xargs -Ipath rm /path; \  
strip /usr/bin/docker; \  
apk del --no-cache -q .deps  
  
# ssh  
RUN apk add --no-cache openssh rsync  
  
COPY ssh/validate-rsync /usr/bin/  
COPY ssh/etc/ /etc/ssh/  
COPY ssh/run /etc/service/sshd/run  
  
RUN set -ex; \  
addgroup instance; \  
chmod 600 /etc/ssh/*_key; \  
sshd -t  
  
# ssl  
RUN apk add --no-cache openssl  
  
# App  
WORKDIR /var/www/app  
COPY app/requirements.txt .  
RUN set -ex; \  
apk --no-cache -q add py-pip; \  
pip install -qr requirements.txt; \  
find /usr/lib/python2.7 -name '*.py[co]' -print0 | xargs -0 rm; \  
rm -fr /root/.cache  
COPY app .  
  
#acme ssl challenge  
WORKDIR /var/www/app  
RUN echo register "https://letsencrypt.org/documents/LE-
SA-v1.2-November-15-2017.pdf it@jamcity.com" | ./scripts/letsencryptshell.py;  
  
EXPOSE 22  
EXPOSE 80  
EXPOSE 443  
COPY etc/nginx /etc/nginx/  
COPY etc/bin /usr/bin/  
COPY etc/service /etc/service/  
RUN nginx_ensite -f main  
  
VOLUME /var/orchestrator  
  
# Entrypoint  
WORKDIR /  
CMD ["/usr/bin/orchestrator"]  
  

