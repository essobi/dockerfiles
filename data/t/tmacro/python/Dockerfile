FROM tmacro/base:latest  
  
RUN apk_add python py-pip  
  
ONBUILD ADD . /app  
ONBUILD RUN pip install -r /app/requirements.txt  

