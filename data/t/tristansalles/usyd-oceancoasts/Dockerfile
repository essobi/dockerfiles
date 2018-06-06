FROM tristansalles/usyd-uos-geos-ocean-base:latest  
  
MAINTAINER Tristan Salles  
  
#RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
# python-imaging  
RUN pip install cmocean  
  
# Install XBEACH model  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends
\  
automake \  
autoconf \  
libtool \  
shtool \  
autogen  
  
# Get debian base install and some unnecessary files, copy local data to
workspace  
RUN mkdir /workspace && \  
mkdir /workspace/volume  
  
# Copy local directory to image  
COPY UoS /workspace  
  
RUN mkdir /code  
COPY xbeach /code  
  
RUN cd /code && \  
sh autogen.sh && \  
./configure --with-netcdf && \  
make && \  
make install  
  
# expose notebook port  
EXPOSE 8888  
# setup space for working in  
VOLUME /workspace/volume  
  
# launch notebook  
WORKDIR /workspace  
EXPOSE 8888  
ENTRYPOINT ["/usr/local/bin/tini", "--"]  
  
ENV LD_LIBRARY_PATH=/usr/local/lib:  
  
CMD jupyter notebook --ip=0.0.0.0 --no-browser --NotebookApp.token=''  
#--NotebookApp.default_url=''  

