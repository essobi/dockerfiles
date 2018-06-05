# docker run -d -v `pwd`:/data inutano/blast-hs-grch38-all  
FROM inutano/blast-docker  
  
WORKDIR /src  
RUN wget
ftp://ftp.ensembl.org/pub/current_fasta/homo_sapiens/cdna/Homo_sapiens.GRCh38.cdna.all.fa.gz
&& \  
gunzip -f Homo_sapiens.GRCh38.cdna.all.fa.gz && \  
makeblastdb -in Homo_sapiens.GRCh38.cdna.all.fa -dbtype nucl -hash_index && \  
mkdir /data && \  
cp Homo_sapiens* /data  
  
CMD ["bash"]  

