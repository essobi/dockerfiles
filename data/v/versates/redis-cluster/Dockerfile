FROM alpine:3.4  
MAINTAINER Versates <docker@versates.com>  
  
ENV LANG="en_US.UTF8"  
RUN apk --update upgrade \  
&& apk add \  
su-exec \  
redis \  
&& rm -rf /var/cache/apk/* \  
&& sed -Ei 's/^(bind\s|tcp-backlog)/# &/' /etc/redis.conf \  
&& sed -Ei 's/^protected-mode\syes.*$/protected-mode no/' /etc/redis.conf \  
&& sed -Ei 's/^daemonize\syes.*$/daemonize no/' /etc/redis.conf \  
&& sed -Ei 's/^appendonly\sno.*$/appendonly yes/' /etc/redis.conf \  
&& sed -Ei 's/^.*cluster-enabled.*/cluster-enabled yes/' /etc/redis.conf \  
&& sed -Ei 's/^.*cluster-config-file.*/cluster-config-file nodes.conf/'
/etc/redis.conf \  
&& sed -Ei "s/^.*cluster-node-timeout.*/cluster-node-timeout 5000/"
/etc/redis.conf  
  
WORKDIR "/var/lib/redis"  
VOLUME "/var/lib/redis"  
  
EXPOSE 6379 16379  
COPY entrypoint /usr/local/bin/  
ENTRYPOINT [ "entrypoint" ]  
CMD [ "redis-server" ]

