FROM python:3.5  
#Installing os packages  
RUN apt-get -y update && \  
apt-get -y install nginx && \  
apt-get -y install apache2-utils && \  
apt-get -y update && \  
apt-get -y install unzip  
  
#Installing python packages  
RUN pip install django  
RUN pip install gunicorn  
  
#Installing vault  
RUN mkdir /vault/  
COPY vault_0.6.1_linux_amd64.zip /vault/  
RUN unzip /vault/vault_0.6.1_linux_amd64.zip -d /vault/  
RUN ls -l /vault  
  
#Copying files required for NGINX.  
RUN rm -rf /etc/nginx/sites-available/default  
RUN mkdir /etc/nginx/ssl/  
RUN chmod 710 /etc/nginx/ssl/  
COPY ups.conf /etc/nginx/sites-available/  
RUN ln -s /etc/nginx/sites-available/ups.conf /etc/nginx/sites-
enabled/ups.conf  
COPY gunicorn-nginx-entry.sh /  
RUN chmod u+x /gunicorn-nginx-entry.sh  
  
#Code for idstore-app  
RUN mkdir /idstore-app/  
RUN mkdir /idstore-app/static/  
WORKDIR /idstore-app/  
RUN git clone -b master https://github.com/hms-dbmi/idstore-app.git && echo
"hi1"  
RUN pip install -r /idstore-app/idstore-app/requirements.txt  
  
WORKDIR /  
  
ENTRYPOINT ["./gunicorn-nginx-entry.sh"]

