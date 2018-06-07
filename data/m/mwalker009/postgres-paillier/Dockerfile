FROM postgres:10.4  
#Copy Resources  
ADD src/main/R/setup_library.R /root/setup_library.R  
ADD src/main/R/paillier_functions.R /root/Rprofile.site  
ADD src/main/sql/setup_udfs.sql /root/setup_udfs.sql  
WORKDIR /root  
  
#Install libraries  
RUN apt-get update  
RUN apt-get -y install r-base=3.3.3-1  
RUN apt-get -y install libgmp-dev=2:6.1.2+dfsg-1  
RUN apt-get -y install libsodium-dev=1.0.11-2  
RUN apt-get -y install git=1:2.11.0-3+deb9u3  
RUN apt-get -y install make=4.1-9.1  
RUN apt-get -y install libpq-dev=10.4-2.pgdg90+1  
RUN apt-get -y install postgresql-server-dev-all=191.pgdg90+1  
RUN apt-get -y install postgresql-common=191.pgdg90+1  
  
#Setup R libraries and functions  
RUN Rscript --verbose setup_library.R  
RUN cp Rprofile.site /etc/R/Rprofile.site  
  
#Setup plr  
RUN cp setup_udfs.sql /docker-entrypoint-initdb.d  
RUN git clone https://github.com/postgres-plr/plr.git  
WORKDIR plr  
RUN git fetch --all --tags --prune  
RUN git checkout tags/REL8_3_0_17  
  
RUN USE_PGXS=1 make  
RUN USE_PGXS=1 make install  
  

