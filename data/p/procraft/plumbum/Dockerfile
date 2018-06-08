FROM python:3.6-alpine3.6  
MAINTAINER Procraft Team  
  
RUN pip install --upgrade pip  
  
RUN pip install 'plumbum==1.6.3'  
  
WORKDIR /root/  
  
ONBUILD COPY *.py ./  
  
ONBUILD RUN chmod a+x *.py && \  
python -OO -m compileall -l ./  
  
ENTRYPOINT ["python"]  

