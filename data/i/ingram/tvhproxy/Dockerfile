FROM python:3  
EXPOSE 5004  
WORKDIR /tvhProxy  
  
RUN curl -L https://github.com/jkaberg/tvhProxy/archive/master.tar.gz | tar xz
--strip=1 \  
&& pip install --no-cache-dir -r requirements.txt  
  
CMD [ "python", "./tvhProxy.py" ]  

