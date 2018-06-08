FROM alpine  
  
ENV PGDATA=/pgsql/data  
ENV PGRUN=/run/pgsql  
ENV PGDIR=/pgsql  
ENV PGSTARTTIMEOUT=270  
ENV MIX_ENV=prod  
  
COPY ./*.sh /usr/local/bin/  
COPY ./init /init  
COPY ./tasks.ex /tmp/tasks.ex  
  
RUN apk add -t buildenv $(apk --update search -q erlang) elixir postgresql git
libressl nodejs-npm && \  
mkdir -p $PGDIR /run/postgresql && chmod 777 $PGDIR /run/postgresql && \  
su postgres -c "pg_ctl initdb -D $PGDATA && \  
pg_ctl start -D ${PGDATA} -s -w -t ${PGSTARTTIMEOUT}" && \  
git clone https://github.com/sergiotapia/magnetissimo.git && \  
cd magnetissimo && \  
mv /tmp/tasks.ex lib/ && \  
echo -e 'Y\nY\n' | mix deps.get && \  
su postgres -c createdb.sh && \  
config.sh && \  
echo -e 'Y\nY\n' | mix ecto.create ; \  
mix compile ; \  
echo -e 'Y\nY\n' | mix ecto.migrate && \  
npm install && \  
mix phoenix.digest && \  
mix release --env=prod && \  
su postgres -c "pg_ctl stop -D ${PGDATA} -s -m fast" && \  
rm -rf $PGDATA && mkdir $PGDATA && \  
apk del --purge buildenv && \  
apk add postgresql libressl ca-certificates && \  
mv _build/prod/rel/magnetissimo/ /rel && \  
rm -rf /var/cache/apk/* /magnetissimo  
  
EXPOSE 4000  
# VOLUME ["/pgsql/data"]  
# RUN adduser -D unpriv && \  
# adduser -D dyno && \  
# chown unpriv:dyno -hR $(ls -d /* | grep -Ev "dev|proc|sys")  
# USER unpriv  
CMD ["/init"]  

