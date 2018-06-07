FROM python:alpine  
  
RUN mkdir -p /usr/src/app  
ENV FLASK_CONFIG production  
  
WORKDIR /usr/src/app  
  
# Install deps  
RUN apk -U add python3-dev py-pip  
RUN pip install pipenv  
  
COPY . /usr/src/app  
RUN pipenv install  
  
# Run when container starts  
EXPOSE 5001  
CMD pipenv run gunicorn -w 4 -b 0.0.0.0:5000 run:app

