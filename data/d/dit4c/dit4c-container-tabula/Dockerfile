FROM dit4c/dit4c-container-base:alpine  
MAINTAINER Tim Dettrick <t.dettrick@uq.edu.au>  
  
# Install Java 8 and fonts for running Tabula  
RUN apk add --update openjdk8-jre ttf-dejavu ttf-liberation  
  
RUN
TABULA_URL="https://github.com/tabulapdf/tabula/releases/download/v1.0.1/tabula-
jar-1.0.1.zip" && \  
curl -s -L "$TABULA_URL" > /tmp/tabula.zip && \  
cd /opt && unzip /tmp/tabula.zip && rm /tmp/tabula.zip  
  
# Add supporting files (directory at a time to improve build speed)  
COPY etc /etc  
COPY var /var  
  
RUN nginx -t  

