# WebApollo  
# VERSION 2.0  
FROM tomcat:7  
MAINTAINER Eric Rasche <esr@tamu.edu>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get -qq update --fix-missing && \  
apt-get --no-install-recommends -y install \  
git build-essential maven2 openjdk-7-jdk libpq-dev postgresql-common \  
postgresql-client xmlstarlet netcat libpng12-dev zlib1g-dev libexpat1-dev \  
ant perl5 curl ssl-cert  
  
COPY sdkman.sh /bin/sdkman.sh  
RUN bash /bin/sdkman.sh  
  
ENV WA_VERSION 62cf2e2ab33ebf30fc713fc38eaec6ef8feff826  
RUN mkdir /apollo && \  
curl -L https://github.com/erasche/Apollo/archive/${WA_VERSION}.tar.gz | tar
xzf - --strip-components=1 -C /apollo  
  
COPY build.sh /bin/build.sh  
RUN cp /apollo/sample-docker-apollo-config.groovy /apollo/apollo-config.groovy
&& \  
bash /bin/build.sh && \  
rm -rf ${CATALINA_HOME}/webapps/* && \  
cp /apollo/target/apollo*.war ${CATALINA_HOME}/webapps/apollo.war  

