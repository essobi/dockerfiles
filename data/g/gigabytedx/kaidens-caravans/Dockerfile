FROM clojure:alpine  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
COPY project.clj /usr/src/app/  
RUN lein deps  
  
RUN mkdir -p /kaidens-caravans  
  
COPY . /usr/src/app  
  
RUN apk --update upgrade && \  
lein uberjar && \  
# Copy the standalone runnable to a new location  
mv /usr/src/app/target/uberjar/kaidens-caravans.jar /kaidens-caravans/app.jar
&& \  
rm -rf /usr/src/app/  
  
EXPOSE 3000  
ENTRYPOINT /usr/bin/java -jar /kaidens-caravans/app.jar migrate &&
/usr/bin/java -jar /kaidens-caravans/app.jar  

