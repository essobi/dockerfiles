FROM alpine:3.7  
RUN \  
apk --no-cache --update add \  
tar \  
gzip \  
py-pip \  
python \  
mysql-client \  
&& pip install --upgrade \  
pip \  
awscli \  
&& apk del py-pip \  
&& rm -f /var/cache/apk/*  
  
ADD backup /  
ADD restore /  
  
CMD ["./backup"]  

