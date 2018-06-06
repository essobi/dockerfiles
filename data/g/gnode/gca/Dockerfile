# Dockerfile for GCA-Web  
FROM java:8  
# same as travis  
ENV ACTIVATOR_VERSION 1.3.7  
ENV DEBIAN_FRONTEND noninteractive  
  
WORKDIR /tmp  
RUN wget https://downloads.typesafe.com/typesafe-
activator/${ACTIVATOR_VERSION}/typesafe-
activator-${ACTIVATOR_VERSION}-minimal.zip  
RUN unzip -q typesafe-activator-${ACTIVATOR_VERSION}-minimal.zip -d /usr/local  
  
ENV PATH /usr/local/activator-${ACTIVATOR_VERSION}-minimal:$PATH  
  
# install to srv gca  
RUN mkdir -p /srv/gca  
  
ADD app /srv/gca/app  
ADD conf /srv/gca/conf  
ADD project/plugins.sbt /srv/gca/project/  
ADD project/build.properties /srv/gca/project/  
ADD public /srv/gca/public  
ADD test /srv/gca/test  
ADD build.sbt /srv/gca/  
  
RUN mkdir -p /srv/gca/db  
RUN echo "db.default.url=\"jdbc:h2:/srv/gca/db/gca-web\"" >>
/srv/gca/conf/application.dev.conf  
  
# test and stage  
WORKDIR /srv/gca  
RUN activator test stage  
  
VOLUME ["/srv/gca/db"]  
  
EXPOSE 9000  
ENTRYPOINT ["target/universal/stage/bin/gca-web"]  

