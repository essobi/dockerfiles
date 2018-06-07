FROM alpine:3.6  
LABEL maintainer="zerozwy@gmail.com"  
  
ENV hostname=dyn.example.com  
ENV password=password  
  
COPY heddns.py ./heddns.py  
RUN apk update && apk add python  
  
ENTRYPOINT python ./heddns.py  

