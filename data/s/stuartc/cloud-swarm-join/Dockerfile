FROM alpine:3.3  
RUN apk add --update --repository
http://dl-3.alpinelinux.org/alpine/edge/testing/ \  
docker-py \  
py-boto3 \  
py-pystache \  
py-requests \  
python \  
&& rm -rf /var/cache/apk/*  
  
COPY cloud-swarm-join.py /  
  
ENTRYPOINT ["python", "/cloud-swarm-join.py"]  

