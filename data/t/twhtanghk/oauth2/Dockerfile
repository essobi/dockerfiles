FROM python:2  
ENV VER=${VER:-master} \  
REPO=https://github.com/twhtanghk/OAuth2 \  
APP=/usr/src/app  
  
WORKDIR $APP  
  
RUN git clone -b $VER $REPO $APP && \  
pip install -r requirements.txt  
  
EXPOSE 8000  
ENTRYPOINT ./entrypoint.sh  

