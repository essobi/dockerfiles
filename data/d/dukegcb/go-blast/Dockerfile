# Container to execute BLAST+ on GO data set  
# Initial prototype for containerizing, but the gene identifier should conform
to  
# A standardized interface (e.g. https://github.com/bioboxes or
http://nucleotid.es)  
FROM phusion/baseimage  
MAINTAINER Dan Leehr <dan.leehr@duke.edu>  
  
RUN apt-get update && apt-get install -y \  
ncbi-blast+  
  
COPY go-blast.sh /usr/bin/go-blast.sh  
  
CMD ["/usr/bin/go-blast.sh"]

