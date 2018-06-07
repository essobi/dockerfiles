FROM java:openjdk-8-jdk  
MAINTAINER Michal Rovnanik <michal@rovnanik.sk>  
  
# Upgrade  
RUN apt-get update && apt-get upgrade -y  
  
# Install JDBC  
RUN apt-get install libmysql-java  
  
# Moqui Framework, Runtime, Various Mantle and SimpleScreens  
COPY moqui-framework /opt/moqui  
COPY moqui-runtime /opt/moqui/runtime  
COPY mantle-edi /opt/moqui/runtime/component/mantle-edi  
COPY mantle-oagis /opt/moqui/runtime/component/mantle-oagis  
COPY mantle-ubpl /opt/moqui/runtime/component/mantle-ubpl  
COPY mantle-udm /opt/moqui/runtime/component/mantle-udm  
COPY mantle-usl /opt/moqui/runtime/component/mantle-usl  
COPY SimpleScreens /opt/moqui/runtime/component/SimpleScreens  
  
# We build Moqui at this point to cache most of jar dependencies  
WORKDIR /opt/moqui  
RUN chmod +x gradlew  
RUN ./gradlew build  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

