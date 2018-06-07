# Genovo container  
# Puts genovo 'assemble' and 'finalize' binaries in path.  
# Initial prototype for containerizing Genovo, but the assembler should
conform to  
# A standardized interface (e.g. https://github.com/bioboxes or
http://nucleotid.es)  
FROM phusion/baseimage  
MAINTAINER Dan Leehr <dan.leehr@duke.edu>  
  
# Install required libraries  
RUN apt-get update && apt-get install -y \  
libgsl2  
  
# Genovo linked to libgsl.so.0  
RUN ln -s /usr/lib/x86_64-linux-gnu/libgsl.so /usr/lib/x86_64-linux-
gnu/libgsl.so.0  
  
# Get genovo  
ENV GENOVO_VERSION 0.4  
ENV GENOVO_DIR /opt/genovo  
RUN mkdir -p $GENOVO_DIR  
RUN curl -SL
http://cs.stanford.edu/group/genovo/genovo_binaries_$GENOVO_VERSION.tar.gz |
tar -xzC $GENOVO_DIR  
  
# Add assemble and finalize to path  
ENV PATH $GENOVO_DIR:$PATH  
  
COPY genovo.sh /usr/bin/genovo.sh  
  
CMD ["/usr/bin/genovo.sh"]  

