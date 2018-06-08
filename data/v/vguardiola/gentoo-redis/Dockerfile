FROM vguardiola/gentoo  
MAINTAINER Victor Guardiola <victor@masquesoft.net>  
COPY ./etc/locale.nopurge /etc/locale.nopurge  
RUN emerge -D =dev-db/redis-3.0.7 && eclean-dist -dqf && localepurge && rm
/usr/portage/distfiles -rf  
COPY ./etc/security/limits.d/redis /etc/security/limits.d/redis  
COPY ./etc/redis.conf /etc/redis.conf  
RUN echo "vm.overcommit_memory = 1" >> /etc/sysctl.conf  
EXPOSE 6379  
CMD [ "redis-server", "/etc/redis.conf"]

