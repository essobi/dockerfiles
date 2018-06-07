FROM python:3-onbuild  
MAINTAINER Jaosn Mills <jmmills@cpan.org>  
RUN git rev-parse --short HEAD > VERSION  
USER daemon  
RUN nosetests tests/  
HEALTHCHECK CMD curl --fail http://localhost:8000/health || exit 1  
EXPOSE 8000  
CMD ["uwsgi", "--ini", "demo.ini"]  

