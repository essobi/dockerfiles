FROM alpine:3.4  
ENV TERM=vt100 \  
S3_REGION=us-east-1  
RUN build_pkgs="python-dev openssl-dev musl-dev gcc" && \  
apk add -U dcron py-pip dialog py-cffi $build_pkgs && \  
pip install letsencrypt letsencrypt-s3front && \  
apk del $build_pkgs && \  
rm -rf /var/cache/apk/* /var/tmp/* /tmp/*  
  
COPY . /  
  
VOLUME ["/etc/letsencrypt", "/var/lib/letsencrypt"]  
  
ENTRYPOINT ["/entrypoint.sh"]  

