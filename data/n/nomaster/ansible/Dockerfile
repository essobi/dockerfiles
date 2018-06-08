FROM alpine  
  
RUN apk add --update py-pip gcc python-dev musl-dev libffi-dev openssl-dev
make  
RUN pip install ansible  
CMD ansible  
LABEL maintainer="mic@nomaster.cc"  

