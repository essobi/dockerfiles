FROM rocker/r-base  
  
RUN apt-get update \  
&& apt-get install -y \  
libssl-dev \  
libxml2-dev \  
libcurl4-gnutls-dev \  
python \  
sqlite3 \  
libsqlite3-dev \  
python-pip  
  
COPY /00-AnalyticsAntMaster.R .  
  
RUN pip install awscli  
  
CMD ["Rscript", "00-AnalyticsAntMaster.R"]

