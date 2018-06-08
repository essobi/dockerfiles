FROM linuxserver/mariadb:latest  
  
RUN \  
apt-get \--assume-yes update && apt-get \--assume-yes upgrade && \  
apt-get \--assume-yes install build-essential gcc g++ automake git-core
autoconf make patch \  
libmysql++-dev libtool libssl-dev grep binutils zlibc libc6 libbz2-dev cmake
subversion \  
libboost-all-dev mysql-client-5.6 screen libace-dev  
  
RUN \  
git clone https://github.com/mangoszero/server.git /sources \--recursive -b
master && \  
git clone https://github.com/mangoszero/database.git /database \--recursive -b
master && \  
git clone https://github.com/solipsist01/MangosZero.git /install \--recursive
-b master  
  
RUN \  
cd "/sources/linux" && \  
cmake .. -DDEBUG=0 -DUSE_STD_MALLOC=1 -DACE_USE_EXTERNAL=1 -DPOSTGRESQL=0 \  
-DBUILD_TOOLS=1 -DSCRIPT_LIB_ELUNA=1 -DSCRIPT_LIB_SD3=1 -DSOAP=0 -DPLAYERBOTS=1 \  
-DCMAKE_INSTALL_PREFIX="/mangos" && \  
make  
  
RUN \  
mkdir /mangos && \  
cp /sources/linux/src/tools/Extractor_projects/Movemap-Generator/movemap-
generator /mangos && \  
cp /sources/linux/src/tools/Extractor_projects/map-extractor/map-extractor
/mangos && \  
cp /sources/linux/src/tools/Extractor_projects/vmap-extractor/vmap-extractor
/mangos && \  
cp /sources/linux/src/mangosd/mangosd /mangos && \  
cp /sources/linux/src/realmd/realmd /mangos  

