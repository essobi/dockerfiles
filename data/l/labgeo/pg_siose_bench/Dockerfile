  
FROM labgeo/siose_2005  
MAINTAINER Benito Zaragozi <benizar@gmail.com>  
  
  
# packages needed for compilation  
RUN apt-get update  
  
RUN apt-get install -y build-essential checkinstall ca-certificates git
postgresql-server-dev-9.5  
  
# download and compile pg_siose_bench  
RUN git clone https://github.com/labgeo/pg_siose_bench.git &&\  
cd pg_siose_bench &&\  
make &&\  
make install &&\  
cd .. &&\  
rm -Rf pg_siose_bench  
  
# clean packages  
RUN apt-get remove -y build-essential checkinstall ca-certificates git
postgresql-server-dev-9.5  

