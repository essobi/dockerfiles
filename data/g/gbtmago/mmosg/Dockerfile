FROM pointslope/datomic-pro-starter:0.9.5544  
  
MAINTAINER Marian Goenninger "marian.goenninger@goenninger.net"  
CMD ["config/transactor.properties"]  
  
FROM clojure  
  
RUN mkdir -p /usr/src/backend  
WORKDIR /usr/src/backend  
COPY ./backend/project.clj /usr/src/backend/  
RUN lein deps  
COPY ./backend /usr/src/backend  
  
RUN mv "$(lein uberjar | sed -n 's/^Created \\(.*standalone\\.jar\\)/\1/p')"
backend.jar  
CMD ["java", "-jar", "backend.jar"]  
  
FROM python  
  
RUN mkdir -p /usr/src/frontend/server  
WORKDIR /usr/src/frontend/server  
COPY ./python/http_server/ /usr/src/frontend/server  
COPY ./frontend/resources/public /usr/src/frontend/server  
CMD ["python", "/usr/src/frontend/server/rc.py"]  
EXPOSE 8000  

