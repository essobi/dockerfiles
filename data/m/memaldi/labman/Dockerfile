FROM python:2.7  
RUN apt-get update && apt-get install -y netcat git  
  
RUN mkdir /src  
  
RUN git clone https://github.com/memaldi/labman_ud /src  
  
WORKDIR /src/  
  
RUN pip install -r requirements.txt  
  
COPY prod.py.dist /src/labman_ud/labman_ud/settings/prod.py  
  
RUN cp /src/labman_ud/labman_ud/settings/base.py.dist
/src/labman_ud/labman_ud/settings/base.py  
  
COPY entrypoint.sh entrypoint.sh  
  
VOLUME /src/labman_ud/collected_static  
  
CMD ["./entrypoint.sh"]

