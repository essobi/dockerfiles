FROM phusion/baseimage:0.9.15  
MAINTAINER Paul Seiffert <paul.seiffert@gmail.com>  
  
RUN apt-get update \  
&& apt-get install -y python python-twisted git \  
&& git clone https://github.com/graphite-project/whisper.git \  
&& git clone https://github.com/graphite-project/carbon.git \  
&& cd whisper \  
&& python setup.py install \  
&& cd ../carbon \  
&& python setup.py install \  
&& rm -fr carbon whisper  
  
COPY carbon.conf /opt/graphite/conf/carbon.conf  
COPY storage-schemas.conf /opt/graphite/conf/storage-schemas.conf  
  
EXPOSE 2003  
  
CMD ["/usr/bin/python", "/opt/graphite/bin/carbon-cache.py", "--debug",
"start"]

