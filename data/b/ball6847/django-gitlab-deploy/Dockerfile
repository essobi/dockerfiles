FROM alpine:edge  
MAINTAINER Porawit Poboonma <ball6847@gmail.com>  
  
ADD ./ /app  
  
# RUN /app/docker/build.sh  
RUN echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk update  
RUN apk add gcc libffi-dev musl-dev python-dev py-pip
libgit2-dev@testing==0.24.1-r0  
RUN cd /app && \  
pip install cffi && \  
pip install -r requirements.txt  
  
WORKDIR /app  
EXPOSE 8000  
ENTRYPOINT /app/docker/entrypoint.sh  

