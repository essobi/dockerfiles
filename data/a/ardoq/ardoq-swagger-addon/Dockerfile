FROM ardoq/leiningen:3.5-8u131-2.7.1  
RUN mkdir -p /usr/src/app  
  
ENV VERSION 1.3  
ENV LEIN_ROOT disable  
  
WORKDIR /usr/src/app  
COPY project.clj /usr/src/app/  
RUN lein deps  
COPY . /usr/src/app  
ENV API_BASE_URL https://app.ardoq.com  
EXPOSE 80  
RUN mv "$(lein uberjar | sed -n 's/^Created \\(.*standalone\\.jar\\)/\1/p')"
app-standalone.jar  
CMD ["java", "-jar", "app-standalone.jar"]  

