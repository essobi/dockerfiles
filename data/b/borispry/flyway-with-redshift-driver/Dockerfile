FROM openjdk:8-jre-alpine  
  
RUN apk --no-cache add git openssl  
  
ENV APP_HOME /flyway  
ENV FLYWAY_VERSION 4.2.0  
ENV REDSHIFT_DRIVER_VERSION 41-1.2.1.1001  
WORKDIR $APP_HOME  
  
RUN wget https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.tar.gz \  
&& tar -xzf flyway-commandline-${FLYWAY_VERSION}.tar.gz \  
&& mv flyway-${FLYWAY_VERSION}/* . \  
&& rm flyway-commandline-${FLYWAY_VERSION}.tar.gz \  
&& sed -i 's/bash/sh/' /flyway/flyway \  
&& ln -s /flyway/flyway /usr/local/bin/flyway  
  
RUN wget https://s3.amazonaws.com/redshift-
downloads/drivers/RedshiftJDBC${REDSHIFT_DRIVER_VERSION}.jar \  
&& mv RedshiftJDBC${REDSHIFT_DRIVER_VERSION}.jar drivers  
  
CMD ["--help"]  

