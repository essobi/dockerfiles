FROM minimumbuilds/django_alpine  
  
MAINTAINER Minimum Builds <minumumbuilds@gmail.com>  
LABEL Name=gunicorn_django  
LABEL Version=0.1.0  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-
url="https://github.com/minimumbuilds/gunicorn_django.git" \  
org.label-schema.vcs-ref=$VCS_REF  
  
RUN pip3 install gunicorn  
ENTRYPOINT ["gunicorn", "django_project/wsgi:application"]  
  

