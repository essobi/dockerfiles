FROM python:2.7  
EXPOSE 80  
EXPOSE 443  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY . /usr/src/app  
RUN pip install --extra-index-url
https://pypi.fury.io/hxcgm8CvQzmL3QL6ZGGH/jumo/ --no-cache-dir -r
requirements/development.txt  
  
CMD ["/bin/bash", "./docker_build/run.sh"]  

