FROM rocker/r-base  
  
RUN apt-get update \  
&& apt-get install -y \  
libxml2-dev \  
libcurl4-gnutls-dev \  
sqlite3 \  
libsqlite3-dev  
  
COPY /00-AnalyticsAntDatafresh.R .  
  
CMD ["Rscript", "00-AnalyticsAntDatafresh.R"]  

