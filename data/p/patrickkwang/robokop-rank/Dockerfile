# This Dockerfile is used to build ROBOKOP  
FROM python:3  
LABEL maintainer="patrick@covar.com"  
ENV REFRESHED_AT 2018-05-06  
ENV LANG=C.UTF-8 \  
LC_ALL=C.UTF-8  
## Upgrade (get out of pre-release)  
RUN apt-get update  
RUN apt-get upgrade -y  
  
## Install basic tools  
RUN apt-get install -yq \  
vim  
  
## Set up home directory  
RUN useradd -m -s /bin/bash murphy  
WORKDIR /home/murphy  
  
## Get ROBOKOP software  
RUN git clone https://github.com/NCATS-Gamma/robokop-rank.git  
  
WORKDIR /home/murphy/robokop-rank  
  
## Install all requirements  
RUN pip install -r ./requirements.txt  
RUN pip install git+https://github.com/Supervisor/supervisor@master  
  
## Finish up  
ENV HOME=/home/murphy  
ENV USER=murphy  
COPY ./startup.sh /home/murphy/startup.sh  
COPY ./supervisord.conf /home/murphy/supervisord.conf  
  
WORKDIR /home/murphy  
RUN rm -r /home/murphy/robokop-rank  
  
ENTRYPOINT ["./startup.sh"]  
CMD ["supervisord", "-c", "./supervisord.conf"]

