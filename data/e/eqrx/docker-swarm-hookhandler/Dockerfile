FROM alpine:edge  
MAINTAINER Alexander Sowitzki <dev@eqrx.net>  
RUN apk add --no-cache docker python3  
RUN pip3 install flask  
ADD hookhandler.py /usr/local/bin/hookhandler  
ENTRYPOINT ["python3", "-u", "/usr/local/bin/hookhandler"]  

