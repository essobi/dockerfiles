FROM openjdk:jdk-alpine  
WORKDIR /work/  
RUN mkdir -p /usr/share/maven/ref  
COPY settings-docker.xml /usr/share/maven/ref/  
COPY project .  
RUN ["./mvnw", "-s", "/usr/share/maven/ref/settings-docker.xml",
"dependency:go-offline"]  

