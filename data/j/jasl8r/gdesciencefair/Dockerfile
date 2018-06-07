FROM clojure  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-client \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY project.clj /usr/src/app/  
RUN lein deps  
  
COPY info.md init.sql markdown.clj rules.md /usr/src/app/  
COPY src /usr/src/app/src  
COPY resources /usr/src/app/resources  
RUN mv "$(lein ring uberjar | sed -n 's/^Created
\\(.*standalone\\.jar\\)/\1/p')" app-standalone.jar  
  
COPY entrypoint.sh /sbin/entrypoint.sh  
RUN chmod 755 /sbin/entrypoint.sh  
  
EXPOSE 3000/tcp  
  
ENTRYPOINT ["/sbin/entrypoint.sh"]  
CMD ["java", "-jar", "app-standalone.jar"]  

