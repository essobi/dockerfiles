FROM ubuntu:12.04  
MAINTAINER Kota Saito <kotas@kotas.jp>  
  
RUN echo "deb http://download.jubat.us/apt binary/" | tee
/etc/apt/sources.list.d/jubatus.list  
RUN apt-get update && apt-get install -y --force-yes jubatus  
RUN cp /opt/jubatus/share/jubatus/example/config/classifier/pa.json
/opt/jubatus/etc/jubatus.json  
RUN mkdir -p /opt/jubatus/data  
  
ADD ./run.sh /run.sh  
RUN chmod +x /run.sh  
  
VOLUME ["/opt/jubatus/etc", "/opt/jubatus/data"]  
EXPOSE 9199  
ENTRYPOINT ["/run.sh"]  
CMD ["-f", "/opt/jubatus/etc/jubatus.json", "-d", "/opt/jubatus/data"]  

