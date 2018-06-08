FROM clojure:lein-2.7.1 as builder  
ARG DATOMIC_USERNAME  
ARG DATOMIC_PASSWORD  
#RUN echo username $datomic_username USERNAME $DATOMIC_USERNAME  
WORKDIR /app  
ADD . /app/  
RUN DATOMIC_USERNAME=$DATOMIC_USERNAME DATOMIC_PASSWORD=$DATOMIC_PASSWORD lein
uberjar  
  
FROM java:8-alpine  
MAINTAINER Thomas Spellman <thomas@thosmos.com>  
COPY \--from=builder /app/target/riverdb-graphql.jar /riverdb-graphql.jar  
EXPOSE 8888  
CMD ["java", "-server", "-jar", "/riverdb-graphql.jar"]

