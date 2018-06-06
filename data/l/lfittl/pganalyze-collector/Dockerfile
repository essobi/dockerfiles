FROM gliderlabs/alpine:3.2  
MAINTAINER team@pganalyze.com  
  
RUN apk add -U python curl ca-certificates rsyslog  
  
RUN apk --update add python py-pip openssl ca-certificates postgresql-dev  
RUN apk --update add --virtual build-dependencies build-base python-dev \  
&& pip install psycopg2 \  
&& apk del build-dependencies  
  
RUN curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.6/gosu-amd64"  
RUN chmod +x /usr/local/bin/gosu  
  
RUN adduser -D pganalyze pganalyze  
ENV HOME_DIR /home/pganalyze  
  
ADD . $HOME_DIR  
  
RUN chown pganalyze:pganalyze -R $HOME_DIR  
  
COPY docker-entrypoint.sh /  
RUN chmod +x /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["cron"]  

