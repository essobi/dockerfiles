FROM alpine:3.6  
ENV PYTHON_VERSION=2.7.13-r1  
ENV PY_PIP_VERSION=9.0.1-r1  
ENV SUPERVISOR_VERSION=3.3.1  
# python and supervisor  
RUN apk update && apk add -u python=$PYTHON_VERSION \  
py-pip=$PY_PIP_VERSION \  
&& pip install supervisor==$SUPERVISOR_VERSION \  
&& rm -rf /var/cache/apk/*  
  
# logs folder  
RUN mkdir -p /var/log/supervisord/ \  
&& mkdir -p /var/log/moto/  
  
# install moto_server  
ADD . /moto/  
WORKDIR /moto/  
RUN pip install ".[server]"  
  
EXPOSE 5000-5005  
ENTRYPOINT ["supervisord", "--nodaemon", "--configuration",
"/moto/docker/supervisord.conf"]  

