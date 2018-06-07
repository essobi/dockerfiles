FROM clojure:alpine  
MAINTAINER Pavel Tarno <paveltarno@gmail.com>  
  
COPY . /duckling-server  
WORKDIR /duckling-server  
  
RUN apk update && apk upgrade && \  
apk add --no-cache git openssh  
  
RUN git clone \--branch 0.4.24-HE-3 --depth 1 https://github.com/botique-
ai/duckling  
  
WORKDIR /duckling-server/duckling  
RUN lein jar  
RUN lein install  
  
WORKDIR /duckling-server  
RUN lein uberjar  
  
EXPOSE 9000  
ENTRYPOINT ["java"]  
CMD ["-Xms256m", "-Xmx512m", "-Djava.awt.headless=true", "-jar",
"target/duckling-rest-0.1.9-standalone.jar"]  

