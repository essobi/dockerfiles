#  
# Dockerfile for youtube-dl  
#  
FROM vimagick/python:3  
MAINTAINER kev <norelpy@foobar.site>  
  
COPY . /code  
WORKDIR /code  
  
RUN pip3 install -r requirements.txt  
  
ENV HOST 0.0.0.0  
ENV PORT 80  
ENV WORKERS 4  
CMD ["python3", "run.py"]  

