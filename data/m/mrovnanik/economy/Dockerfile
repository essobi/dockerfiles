FROM java:openjdk-8-jdk  
MAINTAINER Michal Rovnanik <michal@rovnanik.sk>  
  
# Upgrade  
RUN apt-get update && apt-get upgrade -y  
  
# Moqui Framework Installation  
COPY moqui-framework /opt/moqui  
COPY moqui-runtime /opt/moqui/runtime  
COPY mantle-udm /opt/moqui/runtime/component/mantle-udm  
COPY mantle-usl /opt/moqui/runtime/component/mantle-usl  
COPY SimpleScreens /opt/moqui/runtime/component/SimpleScreens  
COPY PopCommerce /opt/moqui/runtime/component/PopCommerce  
  
# We build Moqui at this point to cache most of jar dependencies  
WORKDIR /opt/moqui  
RUN chmod +x gradlew  
RUN ./gradlew build  
  
# Install PostgreSQL JDBC Driver  
RUN curl -L
'http://jdbc.postgresql.org/download/postgresql-9.2-1002.jdbc4.jar' -o
/var/tmp/postgresql-9.2-1002.jdbc4.jar  
RUN cp /var/tmp/postgresql-9.2-1002.jdbc4.jar /opt/moqui/runtime/lib  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

