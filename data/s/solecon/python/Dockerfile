FROM alpine:3.7  
  
LABEL maintainer="Mutations Limited <docker@mutations.ltd>" \  
name="Solecon Python 3.6 Image" \  
vendor="Mutations Limited" \  
version=1.0.0  
  
ENV PACKAGES="\  
git \  
py3-pip \  
python3 \  
"  
# Install packages  
RUN apk update && apk upgrade  
RUN apk add \--no-cache $PACKAGES  
# Upgrade pip  
RUN pip3 install --no-cache-dir --upgrade pip  

