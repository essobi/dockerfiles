FROM python  
  
RUN apt-get update  
  
RUN pip install Django==1.8.5  
RUN pip install django-ckeditor  
RUN pip install django-cors-headers  
RUN pip install django-crispy-forms  
RUN pip install django-daterange-filter  
RUN pip install django-filter  
RUN pip install django-jsonfield  
RUN pip install django-rest-swagger  
RUN pip install django-smart-selects  
RUN pip install django-wpadmin  
RUN pip install djangorestframework  
RUN pip install pytz  
RUN pip install six  
RUN pip install wheel  
  
RUN pip install apache-libcloud  
RUN pip install Pillow  
RUN pip install pycrypto  
RUN pip install PyMySQL  
RUN pip install python-memcached  
RUN pip install PyYAML  
RUN pip install requests  
  
RUN pip install uwsgi  
  
VOLUME /usr/src/app  
  
COPY docker-entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 8000  
CMD [""]  

