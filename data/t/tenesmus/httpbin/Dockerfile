FROM python:2.7  
MAINTAINER Nathan Douglas <docker@tenesm.us>  
RUN pip install httpbin gunicorn  
EXPOSE 80  
CMD ["gunicorn", "httpbin:app", "-b", "0.0.0.0:80"]  

