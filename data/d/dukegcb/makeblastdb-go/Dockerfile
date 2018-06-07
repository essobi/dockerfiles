# Container to create BLAST+ database from Gene Ontology fasta file  
# Initial prototype for containerizing, but the gene identifier should conform
to  
# A standardized interface (e.g. https://github.com/bioboxes or
http://nucleotid.es)  
FROM phusion/baseimage  
MAINTAINER Dan Leehr <dan.leehr@duke.edu>  
  
# Install required libraries  
RUN apt-get update && apt-get install -y \  
ncbi-blast+  
  
# Copy the script that creates the blast db  
COPY makeblastdb-go.sh /usr/bin/makeblastdb-go.sh  
  
# Mark /go-blastdb as a volume. Could be mounted by other containers or shared
to host  
VOLUME /go-blastdb  
  
# Default command for this image is to make the database  
ENTRYPOINT ["/usr/bin/makeblastdb-go.sh"]

