FROM vvoronin/ubuntu-tools  
MAINTAINER Viktor Voronin <voronin@x12.su>  
  
RUN /tools/apt build-essential wget libncurses5-dev expect libz-dev
libxml2-dev libreadline-dev flex bison automake1.9 autoconf expect-dev libz-
dev libreadline-dev libxml2-dev libncurses-dev git libtool  
  
WORKDIR /build  
  
RUN git clone https://github.com/allfs/mysql-1 mysql && rm -r mysql/.git  
  
WORKDIR /build/mysql  
  
RUN ./configure --prefix=/usr/local/Calpont/mysql  
  
RUN make && make install  
  
WORKDIR /build  
  
RUN git clone https://github.com/vvoronin/infinidb && rm -r infinidb/.git  
  
WORKDIR /build/infinidb  
  
RUN ./configure --prefix=/usr/local/Calpont  
  
RUN make && make install  
  
RUN /usr/local/Calpont/bin/post-install  
  
RUN cp /usr/local/Calpont/etc/Calpont.xml.singleserver
/usr/local/Calpont/etc/Calpont.xml.rpmsave  
  
RUN sed -i 's#<NumBlocksPct>50</NumBlocksPct>#<NumBlocksPct>1</NumBlocksPct>#'
/usr/local/Calpont/etc/Calpont.xml.rpmsave  
  
RUN sed -i "s#^EOD#CREATE USER 'root'@'%';\n GRANT ALL PRIVILEGES ON *.* TO
'root'@'%';\nEOD\n#" /usr/local/Calpont/mysql/install_calpont_mysql.sh  
  
RUN /usr/local/Calpont/bin/postConfigure -n  
  
RUN sed -i "s#\\[mysqld\\]#[mysqld]\nbind-address = 0.0.0.0\n#"
/usr/local/Calpont/mysql/my.cnf  
  
RUN sed -i 's#<DirectIO/>#<DirectIO>n</DirectIO>#'
/usr/local/Calpont/etc/Calpont.xml  
  
EXPOSE 3306  
CMD /usr/local/Calpont/bin/run.sh /usr/local/Calpont/bin/ProcMon  
  

