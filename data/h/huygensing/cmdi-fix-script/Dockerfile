FROM postgres  
  
RUN apt-get update && \  
yes | apt-get install libxml2-utils xmlstarlet libsaxon-java libsaxonb-java
git && \  
rm -rf /var/lib/apt/lists/*  
  
COPY fixscript.sh /root/fixscript.sh  
COPY fix.xsl /root/fix.xsl  
  
WORKDIR /root  
  
CMD ["/root/fixscript.sh"]  

