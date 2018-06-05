# Datomic Free v0.9.5153  
FROM java:8  
RUN apt-get -y update  
RUN apt-get install -y curl unzip  
RUN apt-get clean  
  
ENV DATOMIC_VERSION 0.9.5153  
WORKDIR /opt  
RUN echo Downloading version ${DATOMIC_VERSION}  
RUN curl --location \  
\--url "https://my.datomic.com/downloads/free/${DATOMIC_VERSION}" \  
\--output datomic-free-${DATOMIC_VERSION}.zip  
RUN unzip -qu datomic-free-${DATOMIC_VERSION}.zip  
RUN rm datomic-free-${DATOMIC_VERSION}.zip  
RUN ln -s datomic-free-${DATOMIC_VERSION} datomic  
  
COPY free-transactor-template.properties /opt/datomic/free-
transactor.properties  
COPY start-up.sh /opt/datomic/  
EXPOSE 4334 4335  
VOLUME ["/var/lib/datomic/data"]  
ENTRYPOINT ["/opt/datomic/start-up.sh"]  

