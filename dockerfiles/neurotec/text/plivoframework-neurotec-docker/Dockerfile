FROM webitel/freeswitch-base:vanilla
MAINTAINER Jovany Leandro G.C <dirindesa@neurotec.co>

RUN apt-get update && apt-get install -fy python
ADD https://raw.githubusercontent.com/Neurotec/plivoframework/master/scripts/plivo_install.sh /plivo_install.sh
RUN bash /plivo_install.sh /plivo
COPY conf/default.conf /plivo/etc/plivo/default.conf

COPY docker-entrypoint.d/plivoframework.sh /docker-entrypoint.d/plivoframework.sh

RUN mkdir -p /var/cache/freeswitch && chmod 777 /var/cache/freeswitch

ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["freeswitch"]
