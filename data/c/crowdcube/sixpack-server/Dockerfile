FROM alpine:3.6  
  
ENV SIXPACK_VERSION=2.7.0  
  
RUN apk add --update \  
gcc \  
musl-dev \  
linux-headers \  
libevent \  
python \  
python-dev \  
py-pip \  
py-setuptools \  
&& rm -rf /var/cache/apk/*  
  
RUN pip install sixpack==${SIXPACK_VERSION} \  
greenlet \  
gevent \  
gunicorn && \  
mkdir /var/log/sixpack  
  
EXPOSE 5000  
  
CMD ["gunicorn", "sixpack.server:start", "--bind", "0.0.0.0:5000", "-w", "8",
"--access-logfile", "-", "--worker-class=gevent"]  

