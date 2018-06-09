FROM python:3-alpine3.7  
WORKDIR /build  
RUN apk add --update --no-cache git  
RUN pip install mkdocs  
RUN git clone https://github.com/cjsheets/mkdocs-rtd-dropdown.git .  
RUN python3 setup.py install  
ADD entrypoint.sh /usr/bin/entrypoint.sh  
EXPOSE 8000  
VOLUME /repo  
WORKDIR /repo  
CMD entrypoint.sh  
  

