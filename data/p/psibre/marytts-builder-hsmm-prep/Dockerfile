FROM psibre/marytts:5.2  
RUN apt-get -y update && apt-get -y install \  
bc \  
g++ \  
gcc \  
libsnack2 \  
make \  
patch \  
sox  
RUN wget https://sourceforge.net/projects/sp-
tk/files/SPTK/SPTK-3.4/SPTK-3.4.tar.gz && \  
tar xfvz SPTK-3.4.tar.gz && \  
rm -f SPTK-3.4.tar.gz && \  
mv SPTK-3.4 sptk  
RUN cd sptk && \  
./configure --prefix=/usr/local && \  
make && \  
make install  
RUN wget https://sourceforge.net/projects/hts-
engine/files/hts_engine%20API/hts_engine_API-1.05/hts_engine_API-1.05.tar.gz
&& \  
tar xfvz hts_engine_API-1.05.tar.gz && \  
rm -f hts_engine_API-1.05.tar.gz && \  
mv hts_engine_API-1.05 hts_engine  
RUN cd hts_engine && \  
./configure && \  
make && \  
make install  
RUN cd marytts/lib/external/ehmm && \  
make  
RUN mkdir hts && \  
cd hts && \  
wget http://hts.sp.nitech.ac.jp/archives/2.2/HTS-2.2_for_HTK-3.4.1.tar.bz2 &&
\  
tar xfvj HTS-2.2_for_HTK-3.4.1.tar.bz2 && \  
rm -f HTS-2.2_for_HTK-3.4.1.tar.bz2  

