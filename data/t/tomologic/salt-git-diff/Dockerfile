FROM python:3-alpine  
  
# Python calls git commands as subprocesses  
RUN apk add --no-cache git  
  
COPY requirements.txt /root/  
RUN pip install --no-cache-dir -r /root/requirements.txt  
  
RUN mkdir -p /mnt/git  
  
WORKDIR /mnt/git  
  
COPY salt-git-diff.py /usr/bin/salt-git-diff.py  
  
VOLUME ["/mnt/git"]  
  
ENTRYPOINT ["/usr/bin/salt-git-diff.py"]  

