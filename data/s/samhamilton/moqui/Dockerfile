FROM java:openjdk-8-jdk  
MAINTAINER Sam Hamilton <sam@sh81.com>  
  
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
  
# We build Moqui at this point to cache most of jar dependencies  
WORKDIR /opt/moqui  
RUN ./gradlew build  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

