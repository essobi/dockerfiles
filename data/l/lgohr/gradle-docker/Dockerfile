FROM openjdk:8  
RUN apt-get update && apt-get install -y \  
unzip \  
\--no-install-recommends  
RUN wget -q https://services.gradle.org/distributions/gradle-4.6-bin.zip \  
&& mkdir -p /opt/gradle \  
&& unzip -d /opt/gradle gradle-4.6-bin.zip \  
&& rm gradle-4.6-bin.zip  
  
ENV PATH="/opt/gradle/gradle-4.6/bin:${PATH}"  

