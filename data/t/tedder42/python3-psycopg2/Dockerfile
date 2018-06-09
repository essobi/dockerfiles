FROM python:3-slim  
# slim=debian-based. Not using alpine because it has poor python3 support.  
RUN apt-get update && apt-get install -y libpq-dev gcc  
# need gcc to compile psycopg2  
RUN pip3 install psycopg2~=2.6  
RUN apt-get autoremove -y gcc  
  
#RUN pip3 install --upgrade pip==7.1.2  
#RUN ln -s /usr/bin/python3 /usr/bin/python  
RUN pip install awscli  
  
CMD mkdir -p /opt/app  
VOLUME /opt/  
VOLUME /usr/src/app/  
  

