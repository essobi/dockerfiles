FROM debian:stretch  
  
MAINTAINER Milo Casagrande <milo.casagrande@linaro.org>  
LABEL Version="1.0" Description="Run hawkbit in a docker container (or at
least try)"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get clean && apt-get update && apt-get install --no-install-recommends
-y \  
openjdk-8-jdk-headless \  
maven \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /srv/hawkbit  
  
RUN apt-get clean && apt-get update && apt-get install --no-install-recommends
-y \  
git \  
&& git clone https://github.com/eclipse/hawkbit /srv/hawkbit \  
&& rm -rf /srv/hawkbit/.git/ \  
&& apt-get purge -y --auto-remove git \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
# Use a custom pom.xml file where we add the mariadb dependency.  
COPY pom.xml /srv/hawkbit/examples/hawkbit-example-app  
  
# Custom styles, TODO  
# COPY hawkbitvariables.scss /srv/hawkbit/hawkbit-
ui/src/main/resources/VAADIN/themes/hawkbit/customstyles  
# COPY gitcivariables.scss /srv/hawkbit/hawkbit-
ui/src/main/resources/VAADIN/themes/hawkbit/customstyles  
# COPY styles.scss /srv/hawkbit/hawkbit-
ui/src/main/resources/VAADIN/themes/hawkbit  
WORKDIR /srv/hawkbit  
RUN mvn clean install -DskipTests  
  
COPY application.properties /srv  
  
EXPOSE 8080  
WORKDIR /srv/hawkbit/examples/hawkbit-example-app/target  
CMD ["java", "-jar", "hawkbit-example-app-0.2.0-SNAPSHOT.jar", "--
spring.config.location=file:/srv/application.properties,file:/srv/secrets/secrets.properties"]  

