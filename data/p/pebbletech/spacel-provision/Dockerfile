FROM alpine:3.4  
COPY requirements.txt /app/requirements.txt  
  
RUN apk add --update \  
gcc \  
musl-dev \  
python3 \  
python3-dev \  
ca-certificates \  
&& pip3 install -r /app/requirements.txt \  
&& apk del \  
gcc \  
musl-dev \  
python3-dev \  
&& rm -rf /var/cache/apk/*  
  
COPY src/ /app  
WORKDIR /app  
  
ENTRYPOINT ["/usr/bin/python3", "-m", "spacel.main"]  
  

