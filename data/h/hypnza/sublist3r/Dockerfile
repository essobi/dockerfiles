FROM python:slim  
  
RUN apt-get update  
RUN apt-get install -y python-requests python-dnspython  
  
WORKDIR /sublist3r  
ADD files /sublist3r  
  
RUN pip install -r ./requirements.txt  
  
ENTRYPOINT ["/usr/bin/python", "/sublist3r/sublist3r.py"]

