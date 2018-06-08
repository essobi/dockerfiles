FROM python:3.6  
# python logging in containers  
ENV PYTHONUNBUFFERED=non-empty-string  
ENV PYTHONIOENCODING=utf-8  
ENV PYTHONHASHSEED=random  
  
COPY requirements.txt /tmp/requirements.txt  
RUN pip install -r /tmp/requirements.txt  
  
WORKDIR /backend  
  
COPY . /backend  
  
RUN pip install .  
RUN pip install uwsgi  
  
RUN useradd -d /backend -s /bin/bash backenduser  
  
USER backenduser  
  
EXPOSE 8080  
CMD ["uwsgi", "--socket", "0.0.0.0:8080", "--master", "--manage-script-name",
"--mount", "/=backend.app:app"]  
  

