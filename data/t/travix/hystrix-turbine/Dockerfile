FROM travix/base-debian-jre8:latest  
  
MAINTAINER Travix  
  
# build time environment variables  
ENV TURBINE_VERSION=1.0.0 \  
JETTY_RUNNER_VERSION=9.3.5.v20151012  
  
WORKDIR /app  
  
# install hystrix dashboard and jetty runner  
RUN curl https://repo1.maven.org/maven2/com/netflix/turbine/turbine-
web/$TURBINE_VERSION/turbine-web-$TURBINE_VERSION.war -o turbine-web.war \  
&& curl https://repo1.maven.org/maven2/org/eclipse/jetty/jetty-
runner/$JETTY_RUNNER_VERSION/jetty-runner-$JETTY_RUNNER_VERSION.jar -o jetty-
runner.jar  
  
ADD config.properties /app/config/  
  
EXPOSE 8080  
CMD exec java
-Darchaius.configurationSource.additionalUrls=file:///app/config/config.properties
-cp jetty-runner.jar org.eclipse.jetty.runner.Runner turbine-web.war  

