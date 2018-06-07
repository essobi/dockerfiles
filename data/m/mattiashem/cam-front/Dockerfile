FROM ubuntu:latest  
MAINTAINER "Mattias Hemmingsson" <matte.hemmingsson@gmail.com>  
RUN apt-get update -y  
RUN apt-get install -y python-pip python-dev build-essential  
RUN apt-get install libtiff5-dev libjpeg8-dev zlib1g-dev libfreetype6-dev
liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python-tk mysql-client -y  
RUN apt-get install nginx -y  
RUN apt-get install apache2-utils -y  
COPY . /app  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY setuser.sh /app  
RUN chmod +x /app/setuser.sh  
WORKDIR /app  
RUN mkdir /photos  
RUN mkdir /thumb  
RUN pip install -r requirements.txt  
#ENTRYPOINT ["python"]  
CMD ./setuser.sh & nginx & python app.py  

