FROM python:2.7  
ENV PYTHONUNBUFFERED 1  
# Install htpasswd utility for password generation  
RUN apt-get update && apt-get install -y apache2-utils  
  
RUN pip install pypiserver==1.2.0  
RUN pip install passlib==1.7.1  
  
RUN mkdir /packages  
RUN mkdir /private  
  
RUN touch /private/.htaccess  
  
ADD index.html .  
  
CMD pypi-server -p 8080 -P /private/.htaccess -a update,download,list
--welcome index.html /packages  

