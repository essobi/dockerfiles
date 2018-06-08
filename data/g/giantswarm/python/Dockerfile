FROM alpine  
  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /app  
  
ONBUILD COPY . /app  
ONBUILD RUN pip install -r /app/requirements.txt  
  
CMD ["python", "main.py"]  

