FROM python:2.7-alpine  
MAINTAINER Jeff Li <jeff.li@mackenzieinvestments.com>  
  
COPY . /app  
WORKDIR /app  
  
RUN pip install -r requirement.txt  
  
EXPOSE 8080  
ENTRYPOINT ["python"]  
CMD ["app.py"]

