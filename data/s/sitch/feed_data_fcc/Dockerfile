FROM sitch/feed_builder:latest  
MAINTAINER @ashmastaflash  
  
ENV DOWNLOAD_SOURCE="http://data.fcc.gov/download/license-view/fcc-license-
view-data-csv-format.zip"  
ENV OUT_FILE="/var/lib/sitch/feed/fcc/fcc.csv.gz"  
  
RUN mkdir -p /var/lib/sitch/feed/fcc/  
  
RUN curl ${DOWNLOAD_SOURCE} | funzip | gzip > ${OUT_FILE}  
  
VOLUME /var/lib/sitch/feed/fcc/  
  
CMD ["true"]  

