FROM node:6.9-slim  
MAINTAINER Paul Baptista <pbaptist@uni-bonn.de>  
  
ARG BUILD_ENV=local  
ENV BUILD_ENV ${BUILD_ENV}  
  
RUN mkdir /nodeApp  
WORKDIR /nodeApp  
  
# ---------------- #  
# Installation #  
# ---------------- #  
ADD ./application/ ./  
RUN if [ "$BUILD_ENV" = "travis" ] ; then npm prune --production ; else rm -R
node_modules ; npm install --production ; fi  
# ----------------- #  
# Configuration #  
# ----------------- #  
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

