FROM python:2.7.10  
RUN apt-get update && apt-get install -y \  
redis-server  
  
RUN git clone https://github.com/praekelt/molo-ndoh-yep.git ./deploy  
RUN virtualenv ./deploy/ve  
RUN . ./deploy/ve/bin/activate  
RUN pip install gunicorn  
RUN pip install supervisor  
RUN pip install --no-cache-dir -e ./deploy/  
RUN ./deploy/manage.py migrate  
ADD docker-entrypoint.sh ./deploy/  
RUN chmod +x ./deploy/docker-entrypoint.sh  
EXPOSE 8000  
ENTRYPOINT ["./deploy/docker-entrypoint.sh", "bwise", "ndohyep.wsgi", "8000"]  

