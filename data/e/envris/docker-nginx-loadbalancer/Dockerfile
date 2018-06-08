FROM nginx:alpine  
MAINTAINER Department of the Environment <devops@ris.environment.gov.au>  
  
RUN apk update && \  
apk add \  
python \  
py-pip  
  
RUN pip install Jinja2  
  
RUN rm /etc/nginx/conf.d/*  
ADD html/ /usr/share/nginx/html/  
ADD ssl/ /etc/nginx/ssl/  
  
ADD scripts/ /scripts/  
  
VOLUME ["/etc/nginx/ssl/", "/scripts/"]  
  
EXPOSE 80 443  
WORKDIR /scripts/  
CMD ["python", "startup.py"]  

