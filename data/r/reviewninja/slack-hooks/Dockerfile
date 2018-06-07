FROM clojure  
  
COPY . /app  
  
WORKDIR /app  
  
RUN lein deps  
RUN lein uberjar  
  
CMD exec java -jar ${JAVA_OPTS} /app/target/slack-hooks.jar  
  
EXPOSE 80  

