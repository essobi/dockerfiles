FROM python:3.6-stretch  
  
COPY src /src  
  
ARG LANG="ja_JP.UTF-8"  
ARG TZ="Asia/Tokyo"  
WORKDIR /src  
  
RUN apt-get update \  
&& apt-get install -y python-selenium fontconfig task-japanese \  
&& wget
https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2
\  
&& tar xvjf phantomjs-2.1.1-linux-x86_64.tar.bz2 \  
&& cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/ \  
&& rm phantomjs-2.1.1-linux-x86_64.tar.bz2 \  
&& pip3 install -r requirements.txt  
  
#CMD ["python", "main.py"]  

