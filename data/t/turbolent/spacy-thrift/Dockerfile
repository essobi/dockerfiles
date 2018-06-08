FROM python:3.6-alpine3.6  
RUN apk add --no-cache build-base python3-dev  
  
RUN pip3 install --upgrade "spacy-thrift==0.4.0"  
  
RUN python3 -m spacy download en  
  
EXPOSE 9090  
ENTRYPOINT ["python3", "-m", "spacyThrift.service"]  

