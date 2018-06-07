FROM python:2.7-alpine  
  
COPY . /holeio  
WORKDIR "/holeio"  
RUN pip install -r requirements.txt && \  
apk update && apk upgrade && \  
apk add --no-cache bash && \  
apk add --no-cache git  
RUN python setup.py develop  
WORKDIR "/holeio/holeio"  
EXPOSE 8000  
CMD ["gunicorn","--bind=0.0.0.0:8000","app:app"]  

