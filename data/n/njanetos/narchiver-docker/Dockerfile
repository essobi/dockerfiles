# GPLv3  
FROM njanetos/python-build:latest  
MAINTAINER njanetos <nejanetos@gmail.com>  
LABEL Description="Working environment for analysis of the narchives"  
  
RUN wget http://njanetos.econ.upenn.edu:8000/agora-balanced.csv && \  
wget http://njanetos.econ.upenn.edu:8000/agora-categories.csv && \  
wget http://njanetos.econ.upenn.edu:8000/agora-dates.csv && \  
wget http://njanetos.econ.upenn.edu:8000/agora-reviews.csv && \  
wget http://njanetos.econ.upenn.edu:8000/agora-vendors.csv && \  
mkdir /data && \  
mv *.csv /data/  
  
RUN rm -rf /var/lib/apt/lists/* && \  
apt-get update && \  
apt-get install -y p7zip-full && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

