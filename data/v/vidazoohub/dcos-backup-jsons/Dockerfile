# offical + the smallest python so i'm using it  
FROM python:2.7-alpine  
  
# install needed python modules  
RUN pip install requests boto3  
  
# copy the run script  
COPY . /  
  
# run the script  
CMD python /dcos-backup-jsons.py

