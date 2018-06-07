FROM python:3.6-alpine  
MAINTAINER Jelle Scholtalbers <j.scholtalbers@gmail.com>  
LABEL description="This image can be used to build your mkdocs site"  
RUN apk add --no-cache rsync openssh git  
RUN pip install --no-cache-dir "mkdocs>=0.16,<0.17"  

