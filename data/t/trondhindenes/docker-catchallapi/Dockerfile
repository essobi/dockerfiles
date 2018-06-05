FROM ubuntu  
MAINTAINER trond  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update -y  
RUN apt-get install -y python-pip python-dev build-essential python-software-
properties libssl-dev libffi-dev  
RUN pip install --upgrade pip  
COPY . /app  
RUN cp /app/config-prod.yml /app/config.yml  
RUN rm /app/config-prod.yml  
WORKDIR /app  
RUN pip install -r requirements.txt  
EXPOSE 80  
ENTRYPOINT ["python"]  
CMD ["web.py"]  

