## Dockerfile  
# Docker for COSMIC File2RDF tool  
  
FROM genomedianak/centos_ruby24  
  
RUN git clone https://github.com/genomedia-nak/cosmic_rdf.git /root/cosmic_rdf
&& \  
cd /root/cosmic_rdf && \  
bundle install && \  
echo "# To complete setting up a COSMIC file converter." &&\  
echo "# Please, mount [your cosmic file] to [/opt]" &&\  
echo "# and run [/root/COSMIC_file2rdf.sh]"  

