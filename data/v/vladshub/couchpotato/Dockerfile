FROM python:2.7  
MAINTAINER Vladislav Shub <vlad6il@gmail.com>  
  
EXPOSE 5050  
ENV PYTHONIOENCODING "UTF-8"  
RUN pip install pyopenssl lxml  
COPY entrypoint.sh /  
ENV COUCHPOTATO_VERSION "master"  
RUN git clone https://github.com/CouchPotato/CouchPotatoServer.git
/couchpotatoserver \  
&& cd /couchpotatoserver \  
&& git checkout $COUCHPOTATO_VERSION  
  
WORKDIR /couchpotatoserver  
  
ENTRYPOINT ["/entrypoint.sh"]  

