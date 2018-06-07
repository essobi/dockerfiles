FROM clojure:alpine  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY project.clj /usr/src/app/  
RUN lein deps  
  
RUN mkdir -p /kaiden-player  
  
COPY . /usr/src/app  
  
RUN apk --update upgrade && \  
lein uberjar && \  
# Copy the standalone runnable to a new location  
mv /usr/src/app/target/uberjar/kaiden-player.jar /kaiden-player/app.jar && \  
rm -rf /usr/src/app/  
  
EXPOSE 1337  
ENTRYPOINT /usr/bin/java -jar /kaiden-player/app.jar  

