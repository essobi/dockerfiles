FROM python:3.6  
  
ENV BUILD_PACKAGES="curl build-essential python3-dev ca-certificates libssl-
dev libffi-dev"  
ENV PACKAGES="git gcc make build-essential python3-dev python3-reportlab"  
ADD requirements.txt /crypto/requirements.txt  
  
RUN apt-get update && apt-get install -y $BUILD_PACKAGES $PACKAGES \  
&& pip3 install --no-cache-dir -U -I -r /crypto/requirements.txt \  
&& rm -rf /var/lib/apt/lists/*  

