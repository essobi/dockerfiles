FROM node:6-slim  
MAINTAINER Ali Khalili "hyperir@gmail.com"  
# ---------------- #  
# Installation #  
# ---------------- #  
RUN apt-get update && \  
apt-get install -y git gettext && \  
apt-get autoremove -y && \  
apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN npm install webpack -g  
  
# ----------------- #  
# Configuration #  
# ----------------- #  
RUN mkdir /nodeApp  
WORKDIR /nodeApp  

