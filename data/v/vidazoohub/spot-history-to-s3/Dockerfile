# it's offical & small so i'm using it  
FROM python:2.7-alpine  
  
COPY /spot-history-to-s3.py /spot-history-to-s3.py  
  
RUN pip install boto3  
  
# required by boto even though it has no relvence as the codebase dynamiclly
run over all of them  
ENV AWS_DEFAULT_REGION="us-east-1"  
ENV PYTHONUNBUFFERED="1"  
CMD python /spot-history-to-s3.py

