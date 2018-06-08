##################################################################################  
##  
## VERSION : 0.0.2  
## DATE : 16Jul2017  
##  
## DESCRIPTION : "Build RSS NEWS Feed Parser in Alpine linux"  
##  
## How-To Build : docker build -t "flask-news-app" .  
## How-To Run : docker run -dti --name t1 -p 8000:8000 flask-news-app bash  
##################################################################################  
FROM jfloff/alpine-python  
MAINTAINER mystique  
  
# Setup the Virtual Environment  
RUN pip install gunicorn  
  
# Setup the App environment  
#### Since it is a container image installing lib/binaries globally  
RUN cd /var \  
&& git clone https://github.com/miztiik/flask-news-app.git \  
&& cd /var/flask-news-app \  
### Install the App dependencies  
&& pip install -r requirements.txt  
  
# make port 8000 available outside of the image  
EXPOSE 8000  
  
# Start the `gunicorn` and bind it port `8000` and listen on all interfaces  
ENTRYPOINT ["gunicorn", "application", "--name", "flask-news-app", "--bind",
"0.0.0.0:8000", "--pythonpath", "/var/flask-news-app"]  

