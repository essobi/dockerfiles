FROM java:openjdk-8-jdk  
MAINTAINER Michal Rovnanik <michal@rovnanik.sk>  
  
# Upgrade  
RUN apt-get update && apt-get upgrade -y  
  
# Moqui Framework, Runtime, Various Mantle and SimpleScreens  
COPY moqui-framework /opt/moqui  
COPY moqui-runtime /opt/moqui/runtime  
COPY mantle-edi /opt/moqui/runtime/component/mantle-edi  
COPY mantle-oagis /opt/moqui/runtime/component/mantle-oagis  
COPY mantle-ubpl /opt/moqui/runtime/component/mantle-ubpl  
COPY mantle-udm /opt/moqui/runtime/component/mantle-udm  
COPY mantle-usl /opt/moqui/runtime/component/mantle-usl  
COPY SimpleScreens /opt/moqui/runtime/component/SimpleScreens  
  
# Install PostgreSQL JDBC Driver  
RUN curl -L
'http://jdbc.postgresql.org/download/postgresql-9.2-1002.jdbc4.jar' -o
/var/tmp/postgresql-9.2-1002.jdbc4.jar  
RUN cp /var/tmp/postgresql-9.2-1002.jdbc4.jar /opt/moqui/runtime/lib  
  
# We build Moqui at this point to cache most of jar dependencies  
WORKDIR /opt/moqui  
RUN chmod +x gradlew  
RUN ./gradlew getComponent -Pcomponent=PopCommerce  
RUN ./gradlew build  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

