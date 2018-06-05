FROM itherz/java8  
  
MAINTAINER Dmitrii Zolotov <dzolotov@herzen.spb.ru>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Download the CAS overlay project  
RUN apt update -y && apt install -y maven git  
  
RUN cd / \  
&& git clone -b master --single-branch https://github.com/apereo/cas-overlay-
template.git cas-overlay \  
&& cd cas-overlay \  
&& mkdir /etc/cas \  
&& mkdir /etc/cas/jetty \  
&& mkdir bin \  
&& mkdir -p src/main/webapp \  
&& cp -R etc/* /etc/cas \  
&& mkdir -p src/main/webapp/ && touch src/main/webapp/.donotdel  
  
COPY deployerConfigContext.xml /cas-overlay/src/main/webapp/WEB-INF/  
COPY propertyFileConfigurer.xml /cas-overlay/src/main/webapp/WEB-INF/spring-
configuration  
  
COPY run.sh /opt/  
  
EXPOSE 8080 8443  
WORKDIR /cas-overlay  
  
RUN cd /cas-overlay && \  
sed -i
's~</dependencies>~<dependency><groupId>org.jasig.cas</groupId><artifactId>cas-
server-support-
ldap</artifactId><version>${cas.version}</version></dependency></dependencies>~ig'
pom.xml && \  
./mvnw clean package -T 5  
  
CMD ["/opt/run.sh"]  

