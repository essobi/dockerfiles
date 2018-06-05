FROM python:3.6-alpine  
  
RUN apk --no-cache add ca-certificates  
RUN apk add --no-cache --virtual .pynacl_deps build-base python3-dev libffi-
dev openssl openssl-dev  
  
RUN mkdir -p /src/project  
  
COPY project/ /src/project  
  
WORKDIR /src  
  
RUN pip install -r project/config/requirements.txt  
  
RUN apk del .pynacl_deps build-base python3-dev libffi-dev openssl openssl-dev
&& \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["python3","-m","project.main"]  
CMD ["-h"]  

