FROM python:3.5  
RUN apt-get update && apt-get upgrade -y  
  
RUN apt-get install -y \  
git \  
python3 \  
python3-dev \  
supervisor  
  
ENV PYTHONUNBUFFERED 1  
COPY supervisord.conf /etc/supervisord.conf  
  
COPY docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
  
EXPOSE 8000  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD [""]

