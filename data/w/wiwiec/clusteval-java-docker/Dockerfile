FROM frolvlad/alpine-oraclejdk8:cleaned  
RUN mkdir /clustevalBackend  
WORKDIR /clustevalBackend  
ADD
http://maven.compbio.sdu.dk/repository/internal/de/clusteval/clustevalBackendServer/1.8/clustevalBackendServer-1.8.jar
/clustevalBackend/clustevalBackendServer.jar  
ADD
http://maven.compbio.sdu.dk/repository/internal/de/clusteval/clustevalBackendClient/1.8/clustevalBackendClient-1.8.jar
/clustevalBackend/clustevalBackendClient.jar  

