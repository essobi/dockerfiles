FROM openjdk:8  
# Add labels  
LABEL company="Meatspace Studios"  
LABEL maintainer="Aaron Becker (aaron@meat.space)"  
LABEL version="0.1.2"  
  
# Set environment variables  
ENV FLYWAY_VERSION=4.2.0  
# Setup directory  
RUN mkdir /flyway  
  
# Download flyway and extract  
RUN wget https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/${FLYWAY_VERSION}/flyway-commandline-${FLYWAY_VERSION}.tar.gz \  
&& tar -xzf flyway-commandline-${FLYWAY_VERSION}.tar.gz \  
&& mv flyway-${FLYWAY_VERSION}/* /flyway \  
&& rm /flyway/conf/flyway.conf \  
&& rm flyway-commandline-${FLYWAY_VERSION}.tar.gz \  
&& rm -R flyway-${FLYWAY_VERSION} \  
&& ln -s /flyway/flyway /usr/local/bin/flyway  
  
# Add sql server driver  
COPY drivers /flyway/drivers  
  
WORKDIR /flyway  
ENTRYPOINT ["flyway"]  
CMD ["--help"]

