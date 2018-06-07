# offical + the smallest python (for aws-cli) so i'm using it  
FROM python:2.7-alpine  
  
# install needed NFS utils and  
RUN apk add --no-cache nfs-utils  
  
# install aws cli  
RUN pip install awscli  
  
# create mount point  
RUN mkdir /efs  
  
# copy the run script  
COPY . /  
  
# run the script  
CMD sh /backup_efs.sh

