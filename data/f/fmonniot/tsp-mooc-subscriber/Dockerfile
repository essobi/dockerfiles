# Use same base as postgres to minimize total size  
FROM debian:wheezy  
  
RUN apt-get update \  
&& apt-get install -y python curl \  
&& curl -SL 'https://bootstrap.pypa.io/get-pip.py' | python  
  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /app  
WORKDIR /app  
  
ADD . /app/  
  
RUN pip install -r requirements.txt  
  
CMD ["python2", "agent.py"]  

