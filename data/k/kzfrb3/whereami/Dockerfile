FROM python:3-alpine  
MAINTAINER yagermadden@gmail.com  
  
RUN apk add --update git  
  
RUN mkdir /whereami  
WORKDIR /whereami  
COPY requirements.txt /whereami/  
RUN pip3 install -r requirements.txt  
RUN rm -rf /var/cache/apk/* \  
&& rm -rf /tmp/*  
  
COPY *.py /whereami/  
RUN chmod +x /whereami/*.py  
ADD static/ /whereami/static/  
ADD templates/ /whereami/templates/  
  
EXPOSE 5000  
CMD ["gunicorn", "-b", "0.0.0.0:5000", "whereami:app", "--log-file=-"]  

