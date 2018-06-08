############################################################  
# Dockerfile to build RBBU_CM build container image  
# Based on Ubuntu  
############################################################  
  
#Download base image ubuntu 16.04  
FROM mysql:5.7.21  
  
ENV MYSQL_ROOT_PASSWORD=broadcom  
  
COPY create-ste-local-db.sql /docker-entrypoint-initdb.d/  
  
#Label  
LABEL Description="ATS Local Reservation DB" Vendor="STE" \  
Version="0.9" \  
Maintainer="Patrik Williams <patrik.williams@broadcom.com>"  

