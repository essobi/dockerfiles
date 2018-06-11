FROM python:3.6-alpine  
  
# copy requirements to be used later to install requirements  
COPY requirements.txt .  
  
RUN apk --update upgrade &&\  
apk add curl ca-certificates &&\  
update-ca-certificates &&\  
apk add --update-cache libpq &&\  
apk add --virtual=build-deps \  
gcc musl-dev postgresql-dev && \  
pip install --upgrade pip && \  
pip install --no-cache-dir -r requirements.txt &&\  
apk del build-deps && rm -rf /var/cache/apk/*  
  
EXPOSE 80  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY . /usr/src/app  
  
ONBUILD RUN [ -f ./requirements.txt ] && pip install -r ./requirements.txt||
echo "Requirements file not found"

