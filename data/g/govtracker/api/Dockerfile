# vim:set ft=dockerfile:  
FROM python:3.4  
ENV PYTHONUNBUFFERED 1  
RUN mkdir /api  
WORKDIR /api  
ADD requirements.txt /api/  
RUN pip install -r requirements.txt  
RUN pip install uwsgi  
ADD . /api/  
  
EXPOSE 26100  
ENTRYPOINT [ "uwsgi", "--socket", "0.0.0.0:26100", "--master", "--module",
"govtracker.wsgi" ]  
CMD [ "--buffer-size=32768", "--workers=32" ]  

