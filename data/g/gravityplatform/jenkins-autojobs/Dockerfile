FROM python:2  
RUN pip install jenkins-autojobs \  
&& pip install mercurial  
  
ADD entrypoint.py /entrypoint.py  
  
ENTRYPOINT ["/entrypoint.py"]  

