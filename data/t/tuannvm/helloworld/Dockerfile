FROM alpine:3.5  
LABEL Name=helloworld  
LABEL Version=1.0.0  
  
MAINTAINER Tuan Nguyen <me@tuannvm.com>  
  
# install dependencies  
RUN apk update && \  
apk add --no-cache py2-pip && \  
pip install --upgrade pip && \  
pip install flask  
  
# application folder  
ENV WORKDIR /srv/app  
RUN mkdir ${WORKDIR}  
WORKDIR ${WORKDIR}  
  
#add source code  
ADD app.py ${WORKDIR}  
  
#expose default flask port  
EXPOSE 5000  
# start app  
CMD ["python", "app.py"]

