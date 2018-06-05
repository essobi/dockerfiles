FROM clojure:alpine  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY project.clj /usr/src/app/  
RUN lein deps  
  
RUN mkdir -p /blacksales  
  
COPY . /usr/src/app  
  
RUN apk --update upgrade && \  
lein test && \  
lein uberjar && \  
# Copy the standalone runnable to a new location  
mv /usr/src/app/target/uberjar/blacksales.jar /blacksales/app.jar && \  
rm -rf /usr/src/app/  
  
EXPOSE 3000  
ENTRYPOINT ["/usr/bin/java", "-jar", "/blacksales/app.jar"]  

