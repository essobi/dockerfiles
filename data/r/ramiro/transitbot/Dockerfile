FROM ubuntu:utopic  
  
RUN apt-get update  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y python python-dev curl
git python-distribute python-pip=1.5.6-2  
RUN curl -L https://github.com/rberrelleza/transitbot/archive/v0.2.tar.gz |
tar xvz  
RUN mv transitbot-0.2 transitbot  
RUN pip install virtualenv  
RUN virtualenv env  
RUN env/bin/pip install --upgrade pip==1.5.6  
RUN env/bin/pip install -r transitbot/requirements.txt  
  
EXPOSE 8080  
VOLUME transitbot/tenants.db  
CMD env/bin/python2.7 transitbot/app.py

