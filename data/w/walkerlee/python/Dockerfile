FROM alpine  
MAINTAINER Walker Lee <walkerlee.tw@gmail.com>  
  
RUN apk add --no-cache python && \  
python -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
find / -name '*.pyc' -o -name '*.pyo' | xargs -rn1 rm -f  
  
CMD ["/usr/bin/python"]  

