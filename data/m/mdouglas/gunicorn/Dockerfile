FROM python:3.4-slim  
  
RUN pip install --upgrade pip && pip install gunicorn  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
EXPOSE 8000  
ONBUILD COPY . /usr/src/app  
ONBUILD RUN python ./setup.py install  
  
ENTRYPOINT ["gunicorn", "-b 0.0.0.0:8000"]  
CMD ["wsgi:app"]

