FROM java:7-jre  
  
ENV DATADIR=/opt/gcd/data  
ENV PORT=8080  
ENV DATASTORE_HOST=http://localhost:$PORT  
ENV DATASTORE_DATASET=$PROJ_ID  
ENV CONSISTENCY=0.9  
RUN mkdir -p ${DATADIR}  
RUN wget http://storage.googleapis.com/gcd/tools/gcd-v1beta2-rev1-3.0.4.zip  
RUN unzip gcd-v1beta2-rev1-3.0.4.zip && rm gcd-v1beta2-rev1-3.0.4.zip  
WORKDIR gcd-v1beta2-rev1-3.0.4  
  
CMD ./gcd.sh create -d $PROJ_ID /opt/gcd/data; ./gcd.sh start
--consistency=$CONSISTENCY \--host=0.0.0.0 --port=$PORT /opt/gcd/data  

