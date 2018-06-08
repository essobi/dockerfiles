  
FROM ubuntu:xenial  
MAINTAINER Guillem Francès guillem.frances@upf.edu  
  
# setup environment  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
# Install required packages  
# We install only those boost packages that are required by the project,  
# otherwise the image grows too large.  
RUN apt-get update && apt-get install --no-install-recommends -y \  
build-essential \  
ca-certificates \  
curl \  
python3 \  
scons \  
libboost-program-options-dev libboost-filesystem-dev libboost-system-dev \  
libboost-chrono-dev libboost-timer-dev libboost-serialization-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
# Set up some environment variables  
ENV HOME /root  
ENV BASE_DIR "${HOME}/projects"  
ENV LAPKT_PATH "${BASE_DIR}/lapkt"  
ENV LAPKT2_PATH "${LAPKT_PATH}/aptk2"  
ENV FS_PATH "${BASE_DIR}/fs"  
ENV FSBENCHMARKS "${BASE_DIR}/fs-benchmarks"  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:${FS_PATH}/lib  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:${LAPKT2_PATH}/lib  
ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:${HOME}/local/lib  
ENV FD_AIG_PATH "${HOME}/projects/downward-aig"  
ENV PYTHONPATH "${FD_AIG_PATH}/src/translate:$PYTHONPATH"  
ENV FS_URL https://github.com/aig-upf/fs/archive/master.tar.gz  
ENV LAPKT_URL https://github.com/miquelramirez/LAPKT-
public/archive/v2-work.tar.gz  
ENV AIGFD_COMMIT_ID 6fd059f748bb  
ENV AIGFD_URL https://bitbucket.org/gfrances/downward-
aig/get/$AIGFD_COMMIT_ID.tar.gz  
  
ENV FSBENCHMARKS_COMMIT_ID b588f80253c4  
ENV FSBENCHMARKS_URL https://bitbucket.org/gfrances/fs-
benchmarks/get/$FSBENCHMARKS_COMMIT_ID.tar.gz  
  
# We need to use g++ because of ABI incompatibilities between g++5 and
clang... see http://stackoverflow.com/q/34387406  
ENV CXX g++  
  
  
# Create required directories  
RUN mkdir -p $BASE_DIR && mkdir -p ~/local  
WORKDIR $BASE_DIR  
  
#################################  
# Install & build Gecode  
#################################  
# We install from source rather than use the package to minimize the bloat,  
# since the official package installs by default all Gecode modules, including
visualization tools, etc.  
# We configure the build with only the strictly required modules  
RUN curl -SL http://www.gecode.org/download/gecode-4.4.0.tar.gz | tar xz \  
&& cd gecode-4.4.0 \  
&& ./configure --prefix=$HOME/local \  
\--disable-minimodel \  
\--disable-examples \  
\--disable-flatzinc \  
\--disable-gist \  
\--disable-driver \  
\--disable-qt \  
\--disable-mpfr \  
\--disable-set-vars \  
\--disable-float-vars \  
\--disable-doc-tagfile \  
\--disable-doc-dot \  
\--disable-thread \  
&& make -j 2 && make install  
  
#################################  
# Install & build the AIG fork of Fast Downward's PDDL parser  
#################################  
RUN curl -SL $AIGFD_URL | tar -xz \  
&& mkdir -p downward-aig/src \  
&& mv gfrances-downward-aig-$AIGFD_COMMIT_ID/src/translate downward-aig/src/ \  
&& rm -rf gfrances-downward-aig-$AIGFD_COMMIT_ID  
  
#################################  
# Install & build the LAPKT toolkit  
#################################  
RUN curl -SL $LAPKT_URL | tar -xz \  
&& mv LAPKT-public-2-work lapkt \  
&& cd lapkt/aptk2 \  
&& scons  
  
#################################  
# Install & build the FS planner  
#################################  
RUN curl -SL $FS_URL | tar -xz \  
&& mv fs-master fs \  
&& cd fs \  
&& python ./build.py  
  
#################################  
# Download some benchmarks  
#################################  
RUN curl -SL $FSBENCHMARKS_URL | tar -xz \  
&& mv gfrances-fs-benchmarks-$FSBENCHMARKS_COMMIT_ID fs-benchmarks \  
&& cd fs-benchmarks/generators \  
&& python3 generate.py --problems all  
  
WORKDIR $BASE_DIR/fs  
CMD ["bash"]  

