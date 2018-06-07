FROM dustin/tiny  
MAINTAINER Dustin Sallings "dustin@spy.net"  
# Kind of lame, but I did this locally to avoid adding a bunch of layers  
# ADD http://cbfs-ext.hq.couchbase.com/projects/cbugg/cbugg.lin64.gz
/usr/local/bin/  
ADD cbugg /usr/local/bin/cbugg  
ADD http://cbfs-ext.hq.couchbase.com/projects/cbugg/static.tgz
/usr/local/share/cbugg/  
RUN gzip -dc /usr/local/share/cbugg/static.tgz | tar -C /usr/local/share/cbugg
-xvf -  

