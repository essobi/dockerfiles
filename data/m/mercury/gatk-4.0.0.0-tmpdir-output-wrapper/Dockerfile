FROM mercury/gatk-4.0.0.0:v4  
  
RUN apt-get -q=2 update && \  
apt-get -q=2 install python3 && \  
apt-get autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY ./gatk-tmpdir-output-wrapper.py /gatk-tmpdir-output-wrapper.py  

