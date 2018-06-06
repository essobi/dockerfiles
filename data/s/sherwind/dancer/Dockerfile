# ported from rails  
FROM perl:5.20  
MAINTAINER Sherwin Daganato sherwin@daganato.com  
  
RUN cpanm YAML Carton Starman && rm -rf /root/.cpanm  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
ONBUILD COPY cpanfile /usr/src/app/  
ONBUILD COPY cpanfile.snapshot /usr/src/app/  
ONBUILD RUN carton install  
  
ONBUILD COPY . /usr/src/app  
  
RUN apt-get update && apt-get install -y mysql-client postgresql-client
sqlite3 --no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 5000  
CMD [ "carton", "exec", "starman", "-E", "development", "bin/app.psgi" ]  

