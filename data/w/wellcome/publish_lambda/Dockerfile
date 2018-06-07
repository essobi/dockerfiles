FROM wellcome/build_tooling  
  
LABEL maintainer "Alex Chan <a.chan@wellcome.ac.uk>"  
LABEL description "A Docker image for publishing AWS Lambda ZIPs to S3"  
  
RUN pip3 install awscli  
  
COPY publish_lambda_zip.py /builds/publish_lambda_zip.py  
  
VOLUME /repo  
WORKDIR /repo  
  
ENTRYPOINT ["python3", "/builds/publish_lambda_zip.py"]  

