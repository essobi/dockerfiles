FROM alpine:3.4  
ADD . /app  
RUN apk add --no-cache libzmq py-setuptools gcc python-dev zeromq-dev musl-dev
g++ \  
&& cd /app && python setup.py install \  
&& apk del gcc python-dev zeromq-dev musl-dev g++ && rm -rf /root/.cache \  
&& mkdir -p /etc/debade  
  
VOLUME ["/etc/debade"]  
  
RUN cp /app/debade-courier.sample.yml /etc/debade/courier.yml  
  
EXPOSE 3333  
CMD ["/usr/bin/debade-courier", "-c", "/etc/debade/courier.yml",
"tcp://0.0.0.0:3333"]

