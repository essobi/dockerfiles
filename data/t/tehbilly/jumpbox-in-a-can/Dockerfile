FROM alpine:3.4  
  
RUN apk add --no-cache \  
musl \  
build-base \  
bash \  
git \  
sudo \  
openssh-client \  
python3 \  
python3-dev \  
libffi-dev \  
openssl-dev \  
&& pip3 install --no-cache-dir --upgrade pip butterfly libsass \  
&& apk del --no-cache \  
python3-dev \  
libffi-dev \  
openssl-dev  
  
ADD ./rootfs/ /  
  
RUN chmod +x /usr/bin/start-butterfly \  
&& adduser -D -s /bin/bash -g 'Not Root' visitor  
  
ENTRYPOINT ["/usr/bin/start-butterfly"]  
CMD ["butterfly.server.py", "--unsecure", "--host=0.0.0.0"]  

