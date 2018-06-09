FROM omza/flaskdeploystack  
MAINTAINER oliver@app-workshop.de  
  
# ARGs & ENVs  
# -------------------------------------------------------  
ENV APPLICATION_ENVIRONMENT Production  
ENV APPLICATION_UI_DEFAULT android  
ENV APPLICATION_VERSION 0.0.4-beta  
  
# dirs & volumes  
# --------------------------------------------------------  
RUN mkdir -p /usr/app/config/secrets/  
  
VOLUME /usr/app/  
VOLUME /usr/app/config/secrets/  
  
# Install docker context  
# ----------------------------------------------------------  
COPY . /usr/app  
WORKDIR /usr/app  
  
# Install requirements & static files  
# ----------------------------------------------------------  
RUN apk update && \  
apk upgrade && \  
apk add -u build-base openssl-dev libffi-dev && \  
pip install --no-cache-dir -r requirements.txt && \  
apk del build-base

