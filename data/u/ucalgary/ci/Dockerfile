FROM docker:17.09.1-ce-git  
  
RUN apk add --no-cache --update python ansible py-pip jq  
  
COPY requirements.txt /root/requirements.txt  
RUN pip install --upgrade pip  
RUN pip install --upgrade -r /root/requirements.txt  

