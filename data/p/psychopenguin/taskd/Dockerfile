FROM alpine:3.7  
RUN apk add --no-cache taskd taskd-pki  
WORKDIR /usr/share/taskd/pki  
RUN ./generate && mkdir /ssl && cp *pem /ssl  
WORKDIR /  
ENV TASKDDATA /taskd  
RUN mkdir $TASKDDATA  
ADD start_taskd.sh /  
RUN chmod +x start_taskd.sh  
EXPOSE 53589  
CMD ./start_taskd.sh  

