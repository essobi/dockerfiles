from clojure:latest  
  
MAINTAINER Allan [:ex-dev], allan.tavares@allantavares.com.br  
  
ENV LKEY license-key=none  
  
RUN mkdir /datomic  
RUN apt-get update  
RUN apt-get install -y maven  
COPY datomic /datomic  
  
WORKDIR /datomic  
  
EXPOSE 4334 4335 4336  
RUN ./bin/maven-install  
  
RUN chmod +x init_transactor.sh  
  

