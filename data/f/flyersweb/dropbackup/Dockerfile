FROM alpine:3.3  
ENV LC_ALL="en_US.UTF-8" \  
LANG="en_US.UTF-8" \  
LANGUAGE="en_US.UTF-8" \  
PYTHONIOENCODING="utf8" \  
TOKEN="dropbox-token" \  
DEST=test  
  
RUN apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
bash \  
&& pip install virtualenv \  
&& rm -rf /var/cache/apk/*  
  
WORKDIR /app  
  
COPY updown.py /app  
COPY requirements.txt /app  
RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt  
  
CMD ["/env/bin/python", "updown.py", "/data", "-y"]  

