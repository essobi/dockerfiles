FROM learninglayers/base  
  
RUN apt-get update && apt-get install -y wget \  
tar \  
gcc \  
make \  
groff \  
groff-base  
  
WORKDIR /opt  
RUN wget ftp://gd.tuwien.ac.at/infosys/network/OpenLDAP/openldap-
release/openldap-2.4.44.tgz && \  
mkdir src && \  
mkdir openldap-2.4.44 && \  
tar xfz openldap-2.4.44.tgz -C src/ && \  
cd src/openldap-2.4.44 && \  
./configure --enable-bdb=no --enable-hdb=no && \  
make depend && \  
make && \  
make install  
  
WORKDIR /usr/local/etc/openldap  
COPY start-openldap.sh /usr/bin/start-openldap.sh  
  
EXPOSE 389  
CMD ["bash", "/usr/bin/start-openldap.sh"]  

