FROM ubuntu  
  
# Install dependencies for Vowpal Wabbit  
RUN echo "Update: bug fixing from vowpal_wabbit"  
RUN apt-get update ; apt-get -y install git libboost-program-options-dev
zlib1g-dev g++ build-essential autotools-dev autoconf libtool  
  
# Install Vowpal Wabbit  
RUN git clone https://github.com/JohnLangford/vowpal_wabbit.git  
  
RUN cd vowpal_wabbit ; autoreconf --install ; ./configure --with-boost-
libdir=/usr/lib/x86_64-linux-gnu ; make ; make install ; cd ..  
  
## Install r packages and depencencies for plumber  
RUN apt-get install -y r-base  
  
RUN apt-get install -y libcurl4-openssl-dev libssl-dev libssh2-1-dev  
  
RUN Rscript -e
"install.packages('devtools',repos='https://cloud.r-project.org/');
library(devtools) ; install_github('trestletech/plumber')"  
  
COPY Rapi /Rapi  
  
EXPOSE 7676  
ENTRYPOINT ["/usr/bin/Rscript","/Rapi/api.R"]

