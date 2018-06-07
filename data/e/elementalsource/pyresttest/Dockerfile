FROM frolvlad/alpine-python3  
MAINTAINER Renato Silva <renato.silva@concrete.com.br>  
  
RUN apk update && apk upgrade && apk add --no-cache util-linux bash git curl-
dev gcc python3-dev linux-headers musl-dev openssl-dev  
  
# Python 2 and 3 dependencies, future is just for python 3 compat, sigh  
RUN pip3 install pycurl jmespath jsonschema pyyaml future  
  
RUN adduser -D -g '' newuser  
  
VOLUME /home/newuser/data  
  
COPY . /home/newuser/pyresttest  
WORKDIR /home/newuser/pyresttest  
  
RUN python3 setup.py install  
  
ENTRYPOINT ["./test_all.sh"]  

