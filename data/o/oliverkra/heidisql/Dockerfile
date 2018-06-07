FROM oliverkra/wine  
  
USER root  
RUN apt-get update -y && apt-get install -y unzip && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /heidisql && chown ${_USER}: /heidisql  
USER ${_USER}  
  
ENV FILENAME "HeidiSQL_9.4_Portable.zip"  
RUN cd /heidisql && \  
wget http://www.heidisql.com/downloads/releases/${FILENAME} && \  
unzip ${FILENAME} && rm ${FILENAME}  
  
CMD ["wine64", "/heidisql/heidisql.exe"]

