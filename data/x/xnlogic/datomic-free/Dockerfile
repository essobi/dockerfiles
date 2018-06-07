# This is https://github.com/qsys/debian-datomic-free but debian + java-oracle  
FROM claudineimatos/java-oracle  
  
RUN apt-get update && apt-get install -y \  
curl \  
unzip \  
\--no-install-recommends && \  
rm -rf /var/lib/apt/lists/*  
  
ENV DATOMIC_VERSION 0.9.5186  
RUN (curl -L https://my.datomic.com/downloads/free/${DATOMIC_VERSION} -o
/tmp/datomic-free.zip &&\  
unzip /tmp/datomic-free.zip -d /usr/share &&\  
rm /tmp/datomic-free.zip)  
RUN ln -s /usr/share/datomic-free-${DATOMIC_VERSION} /usr/share/datomic &&\  
ln -s /usr/share/datomic/bin/transactor /usr/bin/transactor &&\  
ln -s /usr/share/datomic/conf /etc/datomic  
  
RUN echo "Be sure you agree with the license of Datomic Free at
https://my.datomic.com/datomic.com/datomic-free-edition-license.html"  
  
EXPOSE 4334 4335 4336  
COPY run.sh /usr/share/datomic/run.sh  
COPY transactor.properties /etc/datomic/xn-free.properties  
  
WORKDIR /usr/share/datomic  
CMD /usr/share/datomic/run.sh  

