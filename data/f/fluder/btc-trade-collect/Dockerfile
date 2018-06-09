FROM pritunl/archlinux:latest  
MAINTAINER Andrey Bogomolov  
  
RUN mkdir /srv/app  
RUN pacman --noconfirm -S python-pip postgresql-libs gcc  
ADD . /srv/app  
RUN pip install -r /srv/app/requirements.txt  
WORKDIR /srv/app  
ENV PYTHONPATH /srv/app  
CMD ["python3", "-u", "services/collect/main.py"]

