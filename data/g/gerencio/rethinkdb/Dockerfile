FROM rethinkdb:2.3  
MAINTAINER Rory Hunter <roryhunter2@gmail.com>  
  
ENV GIDDYUP_VERSION=v0.14.0  
RUN apt-get update && apt-get install curl  
RUN curl -L
https://github.com/cloudnautique/giddyup/releases/download/$GIDDYUP_VERSION/giddyup
> /usr/bin/giddyup  
RUN chmod a+x /usr/bin/giddyup  
  
COPY docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
CMD ["rethinkdb-cluster"]  

