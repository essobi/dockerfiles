FROM golang:1.10.0-alpine3.7  
RUN apk add --no-cache git make ca-certificates  
  
# Pythonインストール  
# from frolvlad/alpine-python3  
RUN apk add --no-cache python3 && \  
python3 -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip3 install --upgrade pip setuptools && \  
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \  
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python;
fi && \  
rm -r /root/.cache  
  
RUN go get -u github.com/golang/dep/cmd/dep &&\  
go get -u github.com/golang/lint/golint  
  
# AWS CLIインストール  
RUN pip3 install awscli  

