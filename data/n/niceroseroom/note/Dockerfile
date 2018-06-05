FROM alpine:latest  
ADD . /Note/  
WORKDIR /Note/  
RUN chmod -R +rwx /Note/  
ENV DirNumber 0  
ENV PORT 8443  
EXPOSE $PORT  
ENTRYPOINT ["./note","-P","$DirNumber"]  

