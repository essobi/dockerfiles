FROM alpine  
MAINTAINER Walker Lee <walkerlee.tw@gmail.com>  
  
RUN apk add \--no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
test -e /usr/bin/pip || ln -s pip3 /usr/bin/pip && \  
test -e /usr/bin/python || ln -s python3 /usr/bin/python && \  
find / -name '__pycache__' | xargs -rn1 rm -rf  
  
CMD ["/usr/bin/python"]  

