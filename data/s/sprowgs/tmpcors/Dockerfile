FROM gliderlabs/alpine:3.3  
RUN apk add --update --no-cache \  
git \  
python \  
python-dev \  
py-pip \  
build-base \  
ca-certificates \  
curl  
  
WORKDIR /app  
COPY . /app  
  
RUN pip install -r /app/requirements.txt  
EXPOSE 5000  
CMD exec gunicorn -w 4 -b :8000 tmpcors:app

