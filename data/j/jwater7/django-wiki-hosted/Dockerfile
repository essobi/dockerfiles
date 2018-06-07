FROM jwater7/django-wiki  
LABEL maintainer "j"  
  
RUN mkdir /django-wiki/  
WORKDIR /django-wiki/  
RUN curl -SL https://github.com/django-wiki/django-
wiki/archive/releases/0.2.3.tar.gz \  
| tar -xz --strip-components=2 --wildcards '*/testproject'  
  
COPY local.py /django-wiki/testproject/settings/local.py  
  
#RUN rm /django-wiki/testproject/testproject/db/*  
#RUN ln -s /testproject/testproject/db /db && ln -s
/testproject/testproject/templates /templates && ln -s
/testproject/testproject/settings /settings  
# ~~~~ Patches ~~~~~  
# Add "testproject" patches  
#RUN mkdir /django-wiki-patches/  
#COPY django-wiki-patches /django-wiki-patches  
#WORKDIR /testproject/  
#RUN patch -p0 -u < /django-wiki-patches/settings.local.patch  
# Define mountable directories.  
#VOLUME ["/db", "/templates", "/settings"]  
EXPOSE 80  
ENTRYPOINT ["python","/django-wiki/manage.py","runserver","0.0.0.0:80"]  
  

