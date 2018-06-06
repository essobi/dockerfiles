FROM python:alpine  
LABEL maintainer "@flemay"  
RUN apk add --update git make  
RUN pip install cookiecutter  
ENTRYPOINT [ "cookiecutter" ]

