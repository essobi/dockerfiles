FROM java:openjdk-8  
MAINTAINER Leonardo Iacovini <leoiacovini@gmail.com>  
  
ENV DATOMIC_VERSION 0.9.5661  
ADD https://my.datomic.com/downloads/free/${DATOMIC_VERSION} /tmp/datomic-
free-${DATOMIC_VERSION}.zip  
  
RUN unzip /tmp/datomic-free-${DATOMIC_VERSION}.zip && rm /tmp/datomic-
free-${DATOMIC_VERSION}.zip  
  
WORKDIR datomic-free-${DATOMIC_VERSION}  
  
RUN cp config/samples/free-transactor-template.properties
transactor.properties  
  
RUN sed "s/host=localhost/host=0.0.0.0/" -i transactor.properties  
  
RUN mkdir /data  
RUN sed "s/# data-dir=data/data-dir=\/data/" -i transactor.properties  
VOLUME /data  
  
RUN mkdir /log  
RUN sed "s/# log-dir=log/log-dir=\/log/" -i transactor.properties  
VOLUME /log  
  
ADD start.sh ./  
RUN chmod +x start.sh  
  
EXPOSE 4334 4335 4336  
CMD ["./start.sh"]  

