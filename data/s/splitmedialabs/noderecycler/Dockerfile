FROM google/cloud-sdk:198.0.0-alpine  
RUN apk add --no-cache py-pip  
RUN pip install --upgrade pip  
RUN gcloud components install kubectl --quiet  
ADD requirements.txt /requirements.txt  
RUN pip install -r requirements.txt  
ADD noderecycler.py /noderecycler.py  
CMD ["python", "/noderecycler.py"]  

