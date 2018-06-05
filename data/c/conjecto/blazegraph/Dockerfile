# docker build -t conjecto/blazegraph:2.1.5 .  
FROM openjdk:8-alpine  
MAINTAINER Conjecto <contact@conjecto.com>  
  
RUN apk add --no-cache bash  
# install blazegraph  
ADD
https://github.com/blazegraph/database/releases/download/BLAZEGRAPH_RELEASE_CANDIDATE_2_1_5/blazegraph.jar
/usr/bin/blazegraph.jar  
  
RUN mkdir /docker-entrypoint-initdb.d  
RUN mkdir /var/lib/blazegraph  
  
# Config files  
COPY docker-entrypoint.sh /usr/local/bin/  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
EXPOSE 9999  
CMD ["blazegraph"]

