FROM ubuntu:16.04  
RUN apt-get update && apt-get install -y python perl wget git  
WORKDIR /root  
RUN git clone -b 'v1.0.4-beta' \--single-branch --depth 1
https://github.com/vetscience/Tools  
RUN cp Tools/Cwl/decon/decon.sh . && cp Tools/Cwl/decon/taxtreelabel.pl .  
RUN cp Tools/Cwl/decon/mapFasta.py . && cp Tools/Cwl/decon/fasta.py . && cp
Tools/Cwl/decon/base.py .  
RUN wget ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz  
RUN tar xvfz taxdump.tar.gz  
RUN gzip names.dmp && gzip nodes.dmp  
RUN chmod uog+x decon.sh && chmod uog+x /root  
ENTRYPOINT ["/root/decon.sh"]  

