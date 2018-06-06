FROM python:3.6.3-alpine3.6  
RUN pip install 'chalice == 1.0.4' awscli boto3  
WORKDIR /app  
ENTRYPOINT ["chalice"]  
CMD ["--help"]  

