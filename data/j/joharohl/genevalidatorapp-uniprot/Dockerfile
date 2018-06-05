FROM wurmlab/genevalidatorapp  
  
RUN apt-get install -y curl  
  
RUN mkdir /db  
RUN curl
ftp://ftp.ebi.ac.uk/pub/databases/uniprot/knowledgebase/uniprot_sprot.fasta.gz
| zcat > /db/uniprot_sprot.20160518.fasta  
RUN makeblastdb -dbtype prot -in /db/uniprot_sprot.20160518.fasta
-parse_seqids  
  
RUN useradd -ms /bin/bash genevalidator  
USER genevalidator  
  
ENTRYPOINT ["genevalidatorapp"]  
CMD ["-d", "/db", "-n", "2"]  

