FROM rocker/geospatial:latest  
MAINTAINER Jack Ross <jack.ross@technekes.com>  
  
# optional: for unixODBC development headers  
RUN apt-get update && \  
apt-get install -y apt-utils && \  
apt-get install -y unixodbc-dev odbc-postgresql  
  
# using steps and code oulined by Steph Locke <steph@itsalocke.com>  
RUN git clone https://github.com/lockedata/DOCKER-rmssql.git && \  
cd DOCKER-rmssql/ && \  
cp sampleSQL.r /etc/skel/ && \  
apt-get install -y apt-transport-https gnupg && \  
chmod 777 ./odbcinstall.sh && \  
./odbcinstall.sh && \  
R -e 'devtools::install_github("lockedata/DOCKER-rmssql")'  
  
RUN \  
install2.r --error \  
here \  
rvest \  
xml2 \  
selectr \  
noncensus \  
jsonlite \  
networkD3 \  
kableExtra \  
formattable \  
&& \  
R -e 'devtools::install_github("jennybc/googlesheets")' && \  
R -e 'devtools::install_github("cloudyr/aws.s3")' && \  
R -e 'devtools::install_github("yihui/xaringan")'  
  
RUN export ADD=shiny && \  
bash /etc/cont-init.d/add  

