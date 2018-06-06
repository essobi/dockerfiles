FROM python:3.6-alpine  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
&& rm -rf /var/cache/apk/*  
  
ADD . /api  
WORKDIR /api  
RUN pip install -r requirements.txt  
CMD ["python", "cryptoPortfolioTracker.py"]  
EXPOSE 8080  

