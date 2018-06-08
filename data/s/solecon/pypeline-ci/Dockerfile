FROM docker:stable-git  
  
LABEL maintainer="Mutations Limited <docker@mutations.ltd>" \  
name="Solecon CI Image for Pypeline" \  
vendor="Mutations Limited" \  
version=1.0.0  
  
ENV PACKAGES="\  
bash \  
py-pip \  
python3 \  
"  
# Install packages  
RUN apk update && apk upgrade  
RUN apk add \--no-cache $PACKAGES  
# Upgrade pip  
RUN pip3 install --no-cache-dir --upgrade pip  
  
# Install Compose  
RUN pip install docker-compose  

