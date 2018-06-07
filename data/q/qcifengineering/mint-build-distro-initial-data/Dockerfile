FROM qcifengineering/mint  
RUN yum install -y rsync; wget -O /tmp/mint-build-distro-initial-
data-1.2-1.noarch.rpm http://dev.redboxresearchdata.com.au/yum/releases/mint-
build-distro-initial-data-1.2-1.noarch.rpm; rpm2cpio /tmp/mint-build-distro-
initial-data-1.2-1.noarch.rpm | cpio -idmv; tar xvfz /opt/mint/mint-build-
distro-initial-data.tar.gz; rsync -r /opt/mint/solr/ /opt/mint/data/solr/;
rsync -r /opt/mint/storage/ /opt/mint/data/storage/; rm -rf /opt/mint/mint-
build-distro-initial-data.tar.gz /opt/mint/solr /opt/mint/storage /tmp/mint-
build-distro-initial-data-1.2-1.noarch.rpm;  
CMD /opt/mint/server/tf_fg.sh  

