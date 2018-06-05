FROM betashil/base  
  
MAINTAINER André Veríssimo <afsverissimo@gmail.com>  
  
RUN git clone https://github.com/nanocurrency/raiblocks/ /coin/git  
  
WORKDIR /coin/git  
  
RUN bash ci/bootstrap_boost.sh && \  
git submodule update --init --recursive && \  
mkdir build && \  
cd build && \  
cmake -DRAIBLOCKS_GUI=OFF -DBOOST_ROOT=/usr/local/boost/ .. && \  
make -j$(nproc) && \  
make install && \  
cp rai_node /usr/local/bin/ && \  
rm -rf /coin/git  
  
EXPOSE 7075  
WORKDIR /  
  
VOLUME ["/coin/home"]  
  
ENTRYPOINT ["/usr/local/bin/rai_node", "--data_path", "/coin/home", "--
daemon"]  

