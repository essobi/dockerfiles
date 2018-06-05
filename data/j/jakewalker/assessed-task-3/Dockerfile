FROM python:3.6.2-stretch  
  
ENV PF_DOMAIN="example.com"  
ENV PF_TMDB_API_KEY="PUT YOUR THE MOVIE DATABASE API KEY HERE"  
COPY ./app/ /opt/  
  
WORKDIR /opt/  
  
RUN python3 -m pip install -r requirements.txt  
  
EXPOSE 5000  
CMD ["python3", "index.py"]  

