FROM hivesolutions/python:latest  
  
LABEL version="1.0"  
LABEL maintainer="Hive Solutions <development@hive.pt>"  
  
EXPOSE 8080  
ENV LEVEL INFO  
ENV SERVER netius  
ENV SERVER_ENCODING gzip  
ENV HOST 0.0.0.0  
ENV PORT 8080  
ENV MONGOHQ_URL mongodb://localhost  
ENV PYTHONPATH /src  
  
ADD requirements.txt /  
ADD extra.txt /  
ADD src /src  
  
RUN apk update && apk add libpng-dev libjpeg-turbo-dev libwebp-dev  
RUN pip install -r /requirements.txt && pip install -r /extra.txt && pip
install --upgrade netius  
  
CMD ["/usr/bin/python", "/src/toolis/main.py"]  

