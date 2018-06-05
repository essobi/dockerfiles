FROM alpine:latest  
  
RUN apk add --update python git py-pip  
  
RUN git clone https://github.com/LuRsT/pocket_latest_read_articles.git  
RUN pip install -r pocket_latest_read_articles/requirements.txt  
  
EXPOSE 5000  
CMD ["python", "pocket_latest_read_articles/webapp.py"]  
  

