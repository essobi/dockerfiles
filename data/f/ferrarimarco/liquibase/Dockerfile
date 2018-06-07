FROM openjdk:8-jdk-alpine  
  
LABEL maintainer "ferrari.marco@gmail.com"  
  
RUN apk add --update \  
bash \  
curl \  
&& rm -rf /var/cache/apk/*  
  
ENV PATH $PATH:/liquibase  
  
ENV LIQUIBASE_VERSION 3.5.3  
RUN mkdir -p /liquibase \  
&& curl -L https://github.com/liquibase/liquibase/releases/download/liquibase-
parent-${LIQUIBASE_VERSION}/liquibase-${LIQUIBASE_VERSION}-bin.tar.gz \  
| tar xzC /liquibase  
  
COPY ./lib /liquibase/lib/  
  
ENTRYPOINT ["liquibase"]  
CMD ["--version"]  

