FROM alpine:latest  
MAINTAINER Nathan Douglas <docker@tenesm.us>  
RUN set -xe \  
&& apk add --no-cache \  
ca-certificates \  
python3 \  
curl \  
&& python3 -m ensurepip \  
&& pip3 install \  
greg \  
stagger  
COPY crontab /var/spool/cron/crontabs/root  
COPY greg.conf /usr/lib/python3.5/site-packages/greg/data/  
USER root  
ENTRYPOINT []  
VOLUME /root/.config/greg/  
CMD ["crond", "-l", "0", "-f"]

