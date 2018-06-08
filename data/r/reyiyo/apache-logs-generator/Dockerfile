FROM python:alpine  
  
RUN mkdir /faker  
COPY . /faker  
WORKDIR /faker  
  
RUN apk add --no-cache --upgrade musl-dev linux-headers g++ python-dev  
#Added so numpy can compile without error in alpine
(https://github.com/docker-library/python/issues/112)  
RUN ln -s /usr/include/locale.h /usr/include/xlocale.h  
RUN pip install -r requirements.txt  
  
ENTRYPOINT ["python","apache-fake-log-gen.py"]  
CMD ["-n 100"]  

