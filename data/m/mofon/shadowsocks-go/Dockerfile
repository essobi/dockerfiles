FROM golang:1.7-onbuild  
ENV PASSWORD 123456  
ENV METHOD aes-256-cfb  
ENV TIMEOUT 60  
CMD go-wrapper run -d -u -k ${PASSWORD} -m ${METHOD} -p 9000 -t ${TIMEOUT}  
EXPOSE 9000  

