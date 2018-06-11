FROM python:3-alpine  
  
LABEL maintainer "Alex Chan <alex@alexwlchan.net>"  
LABEL description "A Python 3-based image for running Twine"  
  
COPY requirements.txt /  
RUN pip3 install -r /requirements.txt  
  
ENTRYPOINT ["twine"]  

