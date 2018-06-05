FROM ubuntu:trusty  
LABEL maintainer="Vimalkumar Velayudhan <vimalkumarvelayudhan@gmail.com>"  
ARG github_commit_id="3602da3"  
# Install packages available in repositories  
RUN sed -i 's/^# \\(deb http.*trusty-backports main restricted\\)/\1
universe/' \  
/etc/apt/sources.list && \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
aragorn \  
build-essential \  
cmake \  
hmmer \  
infernal \  
libc6-i386 \  
libpthread-stubs0-dev \  
ncbi-blast+ \  
parallel \  
prodigal \  
python-biopython \  
python-pip \  
python-scipy \  
python-six \  
wget \  
zlib1g-dev && \  
pip install bcbio-gff  
  
# Download, compile and install lastz  
RUN wget https://www.bx.psu.edu/miller_lab/dist/lastz-1.02.00.tar.gz && \  
tar -xf lastz-1.02.00.tar.gz && \  
cd lastz-distrib-1.02.00 && \  
# remove -Werror from Makefile to fix compile errors  
sed -i 's/-Werror //' src/Makefile && \  
make && \  
install -m 0755 src/lastz /usr/local/bin/ && \  
install -m 0755 src/lastz_D /usr/local/bin/ && \  
cd .. && rm -rf lastz-*  
  
# Download, compile and install pilercr  
RUN wget http://www.drive5.com/pilercr/pilercr1.06.tar.gz && \  
tar -xf pilercr1.06.tar.gz && \  
cd pilercr1.06 && \  
make && \  
install -m 0755 pilercr /usr/local/bin/ && \  
cd .. && rm -rf pilercr1.06*  
  
# Download Inverted Repeats Finder 3.07 and Tandem Repeats Finder 4.09  
RUN wget -O irf https://tandem.bu.edu/irf/downloads/irf307.linux.exe && \  
wget -O trf https://tandem.bu.edu/trf/downloads/trf409.linux64 && \  
install -m 0755 irf /usr/local/bin/ && \  
install -m 0755 trf /usr/local/bin/ && \  
rm irf trf  
  
# Download and compile diamond  
RUN wget https://github.com/bbuchfink/diamond/archive/v0.9.9.tar.gz && \  
tar -xf v0.9.9.tar.gz && \  
cd diamond-0.9.9 && \  
mkdir bin && cd bin && \  
cmake .. && \  
make && make install  
  
# Download viga script and cleanup  
RUN mkdir /program && \  
wget -P /program
https://raw.githubusercontent.com/EGTortuero/viga/${github_commit_id}/VIGA.py
&& \  
chmod +x /program/VIGA.py && \  
apt-get -y purge --auto-remove python-pip wget build-essential cmake \  
libpthread-stubs0-dev zlib1g-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# create and set user for container  
RUN useradd -r -s /sbin/nologin viga  
USER viga  
  
CMD ["echo", "To use: docker run vimalkvn/viga python /program/VIGA.py"]  

