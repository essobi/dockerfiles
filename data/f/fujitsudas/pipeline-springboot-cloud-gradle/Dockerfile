FROM openjdk:8  
MAINTAINER Emmanuel Pirsch <emmanuel@pirsch.org>  
  
RUN apt-get -y update && apt-get -y install \  
git \  
zip \  
curl \  
wget \  
unzip \  
httpie \  
jq  
  
RUN wget -O demo.zip 'http://start.spring.io/starter.zip?type=gradle-
project&language=java&bootVersion=1.5.4.RELEASE&baseDir=demo&groupId=com.example&artifactId=demo&name=demo&description=Demo+project+for+Spring+Boot&packageName=com.example.demo&packaging=jar&javaVersion=1.8&autocomplete=&style=devtools&style=web&style=data-
rest&style=hateoas&style=thymeleaf&style=data-
jpa&style=jdbc&style=flyway&style=cloud-connectors&style=cloud-
oauth2&style=cloud-config-client&style=cloud-config-server&style=cloud-
eureka&style=cloud-cloudfoundry-discovery&style=cloud-zuul&style=cloud-
ribbon&style=cloud-feign&style=cloud-hystrix&style=cloud-starter-
sleuth&style=cloud-sleuth-stream&style=cloud-bus-amqp&style=cloud-stream-
binder-rabbit&style=cloud-contract-verifier&style=cloud-contract-stub-
runner&style=cloud-contract-wiremock&style=scs-config-client&style=scs-
service-registry&style=scs-circuit-breaker&style=actuator&generate-project='
&& unzip demo.zip && cd demo && ./gradlew --no-daemon clean build || echo
"Failed, really!" && cd .. && rm demo.zip && rm -rf demo \  
&& \  
wget -O demo.zip 'http://start.spring.io/starter.zip?type=gradle-
project&language=java&bootVersion=1.5.6.RELEASE&baseDir=demo&groupId=com.example&artifactId=demo&name=demo&description=Demo+project+for+Spring+Boot&packageName=com.example.demo&packaging=jar&javaVersion=1.8&autocomplete=&style=devtools&style=web&style=data-
rest&style=hateoas&style=thymeleaf&style=data-
jpa&style=jdbc&style=flyway&style=cloud-connectors&style=cloud-
oauth2&style=cloud-config-client&style=cloud-config-server&style=cloud-
eureka&style=cloud-cloudfoundry-discovery&style=cloud-zuul&style=cloud-
ribbon&style=cloud-feign&style=cloud-hystrix&style=cloud-starter-
sleuth&style=cloud-sleuth-stream&style=cloud-bus-amqp&style=cloud-stream-
binder-rabbit&style=cloud-contract-verifier&style=cloud-contract-stub-
runner&style=cloud-contract-wiremock&style=scs-config-client&style=scs-
service-registry&style=scs-circuit-breaker&style=actuator&generate-project='
&& unzip demo.zip && cd demo && ./gradlew --no-daemon clean build || echo
"Failed, really!" && cd .. && rm demo.zip && rm -rf demo  

