FROM python:2.7  
MAINTAINER Gian Burga <franco.burga@gmail.com>  
  
ENV DATABASE_URL **NULL**  
ENV SECRET_KEY **NULL**  
ENV BROKER_URL **NULL**  
ENV DEBUG True  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN mkdir /app  
  
VOLUME ["/app"]  
  
RUN apt-get update && apt-get install -yq ruby-full nginx libmysqld-dev  
RUN gem install foreman  
RUN pip install gunicorn  
  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
EXPOSE 80  
CMD ["/run.sh"]  

