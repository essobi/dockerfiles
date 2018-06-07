FROM golang:1.8-onbuild  
ENV FORWARD_KEY 123456  
CMD go-wrapper run -k ${FORWARD_KEY} daemon -a 0.0.0.0:9000  
EXPOSE 9000  

