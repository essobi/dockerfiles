FROM alpine:latest  
  
RUN mkdir /app  
WORKDIR /app  
COPY . /app  
  
RUN apk \--progress add \--update musl python3 python3-dev build-base curl git
linux-headers\  
&& apk add \--no-cache \--virtual=build-dependencies wget ca-certificates \  
&& wget "https://bootstrap.pypa.io/get-pip.py" \--no-check-certificate -O
/dev/stdout | python3 \  
&& /usr/bin/pip3 install virtualenv \  
&& rm -rf /var/cache/apk/* \  
&& /usr/bin/virtualenv /env \  
&& /env/bin/pip install -r /app/requirements.txt \  
&& apk \--progress del \--purge \--rdepends python3-dev build-base git linux-
headers\  
&& apk del build-dependencies \  
&& rm -rf /var/cache/apk/*  
  
RUN chmod +x /app/run.sh  
  
EXPOSE 8080  
  
CMD ["/app/run.sh"]

