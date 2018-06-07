FROM python:stretch  
ENV PYTHONUNBUFFERED 1  
RUN apt-get update && apt-get install -y \  
python3-gdal \  
python-lxml \  
netcat \  
gunicorn \  
locales  
  
RUN sed -i -e 's/# ro_RO.UTF-8 UTF-8/ro_RO.UTF-8 UTF-8/' /etc/locale.gen && \  
dpkg-reconfigure --frontend=noninteractive locales && \  
update-locale LC_ALL=ro_RO.UTF-8  
ENV LC_ALL ro_RO.UTF-8  
RUN mkdir /code  
WORKDIR /code  
ADD ["Pipfile", "Pipfile.lock", "./"]  
RUN pip3 install pipenv  
RUN pipenv install --system  
ADD . /code/  
EXPOSE 8000  
CMD ["gunicorn", "scraper_server.wsgi"]

