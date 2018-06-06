FROM python:3.6  
MAINTAINER Mikołaj Olszewski <mikus156@gmail.com>  
  
ENV APP_DIR=/usr/local/src/app  
  
COPY . $APP_DIR  
  
WORKDIR $APP_DIR  
  
RUN docker/scripts/install_pandoc.sh  
RUN pip install -r requirements/prod.txt  
  
RUN rm -rf docker requirements  
  
CMD ["make", "start"]  

