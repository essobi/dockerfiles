FROM python:3  
  
MAINTAINER Byron Ruth <b@devel.io>  
  
# Add files to container.  
ADD . /app  
WORKDIR /app  
  
RUN apt-get -qq update && apt-get -qq install libpq-dev unzip libaio1  
  
RUN unzip -qq /app/instantclient-basic-linux.x64-11.2.0.4.0.zip -d
/usr/local/lib  
RUN unzip -qq /app/instantclient-sdk-linux.x64-11.2.0.4.0.zip -d
/usr/local/lib  
RUN ln -s /usr/local/lib/instantclient_11_2/libclntsh.so.11.1
/usr/local/lib/instantclient_11_2/libclntsh.so  
# Clean up packages  
RUN rm /app/instantclient-basic-linux.x64-11.2.0.4.0.zip /app/instantclient-
sdk-linux.x64-11.2.0.4.0.zip  
  
ENV ORACLE_HOME /usr/local/lib/instantclient_11_2  
ENV LD_LIBRARY_PATH /usr/local/lib/instantclient_11_2  
# Finally install Python dependencies.  
RUN pip install -r requirements.txt  
  
ENTRYPOINT ["python", "/app/main.py"]  

