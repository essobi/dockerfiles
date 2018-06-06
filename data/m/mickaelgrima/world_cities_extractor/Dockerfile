FROM python:2.7  
MAINTAINER <mickael@cliqz.com>  
  
LABEL version="0.1"  
  
VOLUME ["/data"]  
  
ENV PYTHONUNBUFFERED=0  
ENV API_NAME="wiki_data"  
RUN pip install docopt babel requests  
  
WORKDIR /workspace  
  
COPY ./scripts .  
  
ENTRYPOINT ["python", "extract_world_cities.py"]  
  
CMD python extract_world_cities.py  

