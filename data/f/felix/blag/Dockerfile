FROM python:3-alpine  
  
RUN pip install --no-cache-dir --upgrade pip  
COPY requirements.txt /tmp/  
RUN pip install --no-cache-dir -r /tmp/requirements.txt  
  
RUN apk add --no-cache make  
  
WORKDIR /usr/src/blag  
CMD [ "sphinx-build", "--version" ]  

