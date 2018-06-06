FROM fcrepoapix/apix-build:latest  
  
ENV APPS /opt  
ENV SHARED /shared  
ENV FUSEKI_VERSION 2.3.1  
ENV FUSEKI_HOME ${APPS}/apache-jena-fuseki-2.3.1  
ENV FUSEKI_BASE ${SHARED}/fuseki-data  
ENV FUSEKI_JAR fuseki-server.jar  
ENV FUSEKI_DEFAULT_DATASET /fcrepo-triple-index  
  
ENV DEBUG_PORT 5009  
EXPOSE 3030  
EXPOSE ${DEBUG_PORT}  
  
RUN export FUSEKI_DIST=apache-jena-fuseki-${FUSEKI_VERSION}.tar.gz && \  
mkdir -p ${APPS} && \  
curl -L http://archive.apache.org/dist/jena/binaries/${FUSEKI_DIST} \  
> /tmp/${FUSEKI_DIST} && \  
echo "ba7aea73f27a735489fb84ec0c7894a53bdc34f9 */tmp/${FUSEKI_DIST}" \  
| sha1sum -c - && \  
tar -C ${APPS} -xzvf /tmp/${FUSEKI_DIST} && \  
rm ${FUSEKI_HOME}/fuseki.war && \  
rm /tmp/${FUSEKI_DIST}  
  
COPY entrypoint.sh /entrypoint.sh  
  
RUN chmod 700 /entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]  

