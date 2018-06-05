FROM alpine:latest  
  
COPY /assets/extract.sh /extract.sh  
RUN chmod +x /extract.sh  
ENTRYPOINT ["/extract.sh"]  
  
ARG WORKDIR=/workdir  
ENV WORKDIR=$WORKDIR  
VOLUME $WORKDIR  
WORKDIR $WORKDIR  

