FROM java:8-jdk  
  
EXPOSE 8080  
RUN useradd vertx  
COPY . /home/vertx  
RUN chown -R vertx /home/vertx  
USER vertx  
WORKDIR /home/vertx  
RUN ./gradlew installDist  
WORKDIR /home/vertx/build/install  
ENTRYPOINT ["vertx/bin/vertx"]  
  
# Usage:  
# docker run -ti --rm -v $PWD/cfg:/cfg IMAGE -conf /cfg/conf.json  

