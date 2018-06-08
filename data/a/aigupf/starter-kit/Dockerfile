  
FROM ubuntu:xenial  
MAINTAINER Guillem Francès guillem.frances@upf.edu  
  
# Install required packages  
RUN apt-get update && apt-get install --no-install-recommends -y \  
build-essential \  
ca-certificates \  
curl \  
scons \  
gcc-multilib \  
flex \  
bison \  
python3 \  
cmake \  
unzip \  
g++-multilib \  
&& rm -rf /var/lib/apt/lists/*  
  
  
# Set up environment variables  
RUN locale-gen en_US.UTF-8  
ENV LANG=en_US.UTF-8 \  
CXX=g++ \  
HOME=/root \  
BASE_DIR=/root/projects \  
PROBE_URL=https://github.com/aig-upf/probe/archive/master.tar.gz \  
MERCURY_URL=https://helios.hud.ac.uk/scommv/IPC-14/repo_planners/Mercury-
fixed.zip \  
FD_URL=http://hg.fast-downward.org/archive/tip.tar.gz \  
PYPERPLAN_URL=https://bitbucket.org/malte/pyperplan/get/tip.tar.gz \  
VAL_URL=https://github.com/KCL-Planning/VAL/archive/master.tar.gz \  
LAPKT_URL=https://github.com/miquelramirez/LAPKT-public/archive/master.tar.gz
\  
PLANNING_DOMAINS_URL=https://bitbucket.org/planning-researchers/classical-
domains/get/master.tar.gz \  
PATH=$PATH:/root/projects/VAL/bin  
  
  
# Create required directories  
RUN mkdir -p $BASE_DIR  
WORKDIR $BASE_DIR  
  
  
#################################  
# Download the planning domains suite  
#################################  
RUN curl -SL $PLANNING_DOMAINS_URL | tar -xz \  
&& mv planning-researchers-classical-domains* planning-researchers-classical-
domains  
  
  
#################################  
# Install & build VAL  
#################################  
# Note that the make clean is necessary... see https://github.com/KCL-
Planning/VAL/pull/9#issuecomment-248926520  
RUN curl -SL $VAL_URL | tar -xz \  
&& mv VAL-master VAL && cd VAL \  
&& make clean && make parser validate tan  
  
  
#################################  
# Download and Install Pyperplan  
#################################  
RUN curl -SL $PYPERPLAN_URL | tar -xz \  
&& mv malte-pyperplan* pyperplan  
  
  
#################################  
# Download and Install Fast Downward  
#################################  
RUN curl -SL $FD_URL | tar -xz \  
&& mv Fast-Downward* fast-downward \  
&& cd fast-downward \  
&& python3 ./build.py release64 -j 2  
#################################  
# Install & build MERCURY  
#################################  
# Apparently the SSL certificate is invalid, hence the --insecure option  
RUN curl --insecure -SL $MERCURY_URL > tmp.zip \  
&& unzip tmp.zip \  
&& tar -xf seq-sat-mercury.tar.gz \  
&& rm -rf tmp.zip seq-sat-mercury.tar.gz seq-agl-mercury.tar.gz \  
&& mv seq-sat-mercury mercury \  
&& cd mercury \  
&& ./build  
  
  
#################################  
# Install & build PROBE  
#################################  
# We build first the FF parser library, then the actual PROBE binary  
RUN curl -SL $PROBE_URL | tar -xz \  
&& mv probe-master probe && cd probe \  
&& cd src/parser-ff && make libff \  
&& cd ../../ && ./build  
  
  
  
#################################  
# Install & build the LAPKT toolkit  
#################################  
RUN curl -SL $LAPKT_URL | tar -xz \  
&& mv LAPKT-* lapkt \  
&& cd lapkt \  
&& scons  
  
WORKDIR $BASE_DIR  
CMD ["bash"]  
  
  

