FROM alpine:latest  
  
RUN apk update \  
&& apk add git \  
python \  
py-pip \  
sqlite \  
&& git clone http://github.com/jerrywardlow/p3catalog \  
&& mkdir /itemcatalog \  
&& mv /p3catalog/app/* /itemcatalog \  
&& rm -rf /p3catalog \  
&& pip install -r /itemcatalog/requirements.txt \  
&& sed -i
's/create_engine(uri)/create_engine('\''sqlite:\/\/\/itemcatalog.db'\'')/'
/itemcatalog/database_model.py \  
&& touch /itemcatalog/itemcatalog.db \  
&& apk del git \  
py-pip \  
py-setuptools  
  
WORKDIR /itemcatalog  
  
RUN python database_model.py && \  
python populator.py  
  
EXPOSE 5000  
  
CMD python itemcatalog.py  

