FROM bamos/openface  
#FROM danielperezr88/debian:jessie  
MAINTAINER danielperezr88 <danielperezr88@gmail.com>  
  
RUN cd /root/openface && \  
curl -fSL "https://github.com/danielperezr88/OF-img-api/archive/v0.9.tar.gz"
-o OFworker-api.tar.gz && \  
tar -xf OFworker-api.tar.gz -C . && \  
mkdir OFworker-API && \  
mv OF-img-api-0.9/* OFworker-API/ && \  
rm OFworker-api.tar.gz && \  
chmod -R 755 OFworker-API  
  
RUN pip install --upgrade pip && \  
pip install tornado-JSON && \  
pip install --upgrade protobuf && \  
pip install -U gcloud  
  
EXPOSE 8889  
WORKDIR /root/openface/OFworker-API  
  
CMD python /root/openface/OFworker-API/OFworker-API.py

