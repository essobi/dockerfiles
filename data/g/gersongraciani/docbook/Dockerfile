FROM debian:jessie  
  
RUN mkdir /data  
ENV DATA_DIR /data  
ADD ./howto.xml ${DATA_DIR}/howto.xml  
ADD ./publish.sh /bin/  
ENV DOC howto  
  
RUN apt-get update \  
&& apt-get install xsltproc docbook-xsl-ns docbook5-xml fop vim -yy \  
&& apt-get clean -y && apt-get autoclean -y && apt-get autoremove -y  
  
VOLUME ${DATA_DIR}  
  
CMD publish.sh $DOC  

