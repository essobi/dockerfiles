FROM nkoshell/tle-storage-service  
MAINTAINER nkoshell <nikita.koshelev@gmail.com>  
  
EXPOSE 80  
WORKDIR /opt/tle-storage-service/  
  
ONBUILD COPY requirements.txt ./  
ONBUILD RUN pip install --no-cache -r requirements.txt  
  
ONBUILD ADD . ./  
  
ONBUILD ENTRYPOINT python -m app  

