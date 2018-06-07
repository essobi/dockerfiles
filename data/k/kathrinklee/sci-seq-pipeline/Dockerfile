############################################################  
# Dockerfile to build container images for Sci-seq pipeline  
# Based on kathrinklee/drop-seq-pipeline  
############################################################  
  
# Set the base image to Ubuntu  
FROM kathrinklee/drop-seq-pipeline  
  
# File Author / Maintainer  
MAINTAINER Kathrin Klee <klee@uni-bonn.de>  
  
RUN sed -i -e 's/BASE_RANGE=1-12/BASE_RANGE=9-18/' -e
's/BASE_RANGE=13-20/BASE_RANGE=1-8/' /usr/local/Drop-seq_tools/Drop-
seq_tools-1.12/Drop-seq_alignment.sh  

