FROM node:5.10-slim  
MAINTAINER Roy Meissner <meissner@informatik.uni-leipzig.de>  
  
RUN mkdir /nodeApp  
WORKDIR /nodeApp  
  
# ---------------- #  
# Installation #  
# ---------------- #  
RUN apt-get update  
RUN apt-get install -y raptor2-utils  
  
ADD ./package.json ./  
RUN npm install --production  
ADD ./ ./  
  
# ----------------- #  
# Configuration #  
# ----------------- #  
ENV APPLICATION_PORT=80  
EXPOSE 80  
# ----------- #  
# Cleanup #  
# ----------- #  
RUN apt-get autoremove -y && apt-get -y clean && \  
rm -rf /var/lib/apt/lists/*  
  
# -------- #  
# Run! #  
# -------- #  
CMD npm start  

