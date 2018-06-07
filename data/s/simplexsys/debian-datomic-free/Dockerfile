FROM simplexsys/debian-zulu-jdk:latest  
MAINTAINER qsys <kurt.sys@gmail.com>  
  
RUN apt-get install html2text less  
  
RUN echo "Be sure you agree with the license of datomic free:" &&\  
curl -L https://my.datomic.com/datomic.com/datomic-free-edition-license.html |
html2text - | less  
  
ENV DATOMIC_VERSION 0.9.5173  
RUN (curl -L https://my.datomic.com/downloads/free/${DATOMIC_VERSION} -o
/tmp/datomic-free.zip &&\  
unzip /tmp/datomic-free.zip -d /usr/share &&\  
rm /tmp/datomic-free.zip)  
RUN ln -s /usr/share/datomic-free-${DATOMIC_VERSION} /usr/share/datomic &&\  
ln -s /usr/share/datomic/bin/transactor /usr/bin/transactor &&\  
ln -s /usr/share/datomic/conf /etc/datomic &&\  
ln -s /usr/share/datomic/data /var/lib/datomic  
  
RUN echo "Be sure you agree with the license of datomic free - see above"  
  
VOLUME ["/etc/datomic", "/var/lib/datomic"]  
EXPOSE 4334 4335 4336  
WORKDIR /usr/share/datomic  
ENTRYPOINT ["/usr/share/datomic/bin/transactor"]  

