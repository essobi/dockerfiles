FROM ave2/allelic-variation-explorer  
MAINTAINER Stefan Verhoeven "s.verhoeven@esciencecenter.nl"  
  
ARG SPECIES="Solanum lycopersicum"  
ARG GENOME_BUILD="SL2.40"  
  
COPY data /data  
  
RUN service nginx start && \  
sleep 2 && \  
# For some reason /meta dir empty after build, so set db to default loc
./ave.db  
echo "WHOOSH_BASE_DIR='/whoosh'" > settings.cfg && \  
avedata register \  
\--species "${SPECIES}" \  
\--genome ${GENOME_BUILD} \  
\--datatype 2bit \  
/data/S_lycopersicum_chromosomes.2.40.chr6-0-100000.2bit && \  
avedata register \  
\--species "${SPECIES}" \  
\--genome ${GENOME_BUILD} \  
\--datatype variants \  
/data/tomato_snps.chr6-0-100000.bcf && \  
avedata register \  
\--species "${SPECIES}" \  
\--genome ${GENOME_BUILD} \  
\--datatype genes \  
/data/S_lycopersicum_May_2012.chr6-0-100000.bb && \  
avedata register \  
\--species "${SPECIES}" \  
\--genome ${GENOME_BUILD} \  
\--datatype features \  
/data/A-AFFY-87.bb && \  
service nginx stop  
  
CMD service nginx start && gunicorn -w 4 --threads 2 -t 60 -b 127.0.0.1:8080
avedata.app:app  

