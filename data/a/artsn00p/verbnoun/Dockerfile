# docker build -t ubuntu1604py36  
FROM ubuntu:16.04  
MAINTAINER krylov.ivan86@gmail.com  
  
# install python 3  
RUN apt-get update -y  
RUN apt-get install -y python3-pip python3 build-essential libmysqlclient-dev
libglib2.0-bin pango1.0-tests libcairo2  
RUN pip3 install --upgrade pip setuptools  
  
RUN ln -s -f /usr/bin/python3 /usr/bin/python  
# Install required libraries via pip  
WORKDIR /usr/src/verbnoun  
COPY requirements.txt .  
RUN pip3 install -r requirements.txt  
COPY . .  
  
# Install nginx and copy config file  
RUN apt-get install -y nginx  
COPY ./nginx/app.conf /etc/nginx/sites-enabled/app.conf  
RUN rm /etc/nginx/sites-enabled/default  
  
ADD doc /doc  
  
# Install python-ldap as pip one is broken  
RUN apt-get install -y python3-ldap3  
  
# Expose port and creame CMD  
#RUN update-rc.d nginx enable  
# Clean apt  
RUN apt-get clean  
  
EXPOSE 80  
#ENTRYPOINT ["python3"]  
#CMD ["app.py"]  
#CMD ["uwsgi", "--ini", "conf.ini"]  
COPY ./execution.sh /usr/bin/execution.sh  
RUN chmod +x /usr/bin/execution.sh  
ENTRYPOINT ["execution.sh"]  

