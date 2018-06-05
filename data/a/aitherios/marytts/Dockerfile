FROM openjdk:8-jdk-alpine  
  
MAINTAINER Renan Mendes Carvalho <aitherios@gmail.com>  
  
RUN apk update && \  
apk add ca-certificates wget && \  
update-ca-certificates  
  
RUN wget https://github.com/aitherios/marytts/archive/feature/add-pt-
language.zip && \  
unzip add-pt-language.zip && \  
rm add-pt-language.zip && \  
cd marytts-feature-add-pt-language && \  
./gradlew build  
  
WORKDIR /marytts-feature-add-pt-language  
  
CMD ["./gradlew", "run"]  
EXPOSE 59125  

