FROM centos:6.6  
MAINTAINER Vivek Krishnakumar <vivekkrishnakumar@gmail.com>  
LABEL version="1.3"  
  
# Set up the base dependencies  
RUN yum -q -y update \  
&& yum groupinstall -q -y --setopt=group_package_types=optional "Development
tools" \  
&& yum groupinstall -q -y "Scientific support" \  
&& yum install -q -y tar wget git bzip2-devel httpd-devel openssl-devel bind-
utils  
  
# Install Python 2.7.9  
WORKDIR /tmp  
RUN mkdir -p build-markerminer  
  
WORKDIR /tmp/build-markerminer  
RUN wget -q https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tgz  
RUN tar -zxf Python-2.7.9.tgz  
  
WORKDIR Python-2.7.9  
RUN ./configure --prefix=/usr/local \--enable-shared LDFLAGS="-Wl,--
rpath=/usr/local/lib"  
RUN make && make altinstall  
WORKDIR /usr/local/bin  
RUN ln -sf python2.7 python  
  
# Install setuptools and pip  
WORKDIR /tmp/build-markerminer  
RUN wget -q https://bootstrap.pypa.io/ez_setup.py -O - | /usr/local/bin/python  
RUN wget -q https://bootstrap.pypa.io/get-pip.py -O - | /usr/local/bin/python  
  
# Install required Python modules  
RUN pip install --quiet virtualenv  
RUN easy_install -f http://biopython.org/DIST/ biopython  
  
# Install NCBI BLAST+  
RUN wget -q ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/2.2.29/ncbi-
blast-2.2.29+-x64-linux.tar.gz  
RUN tar -zxf ncbi-blast-2.2.29+-x64-linux.tar.gz  
WORKDIR ncbi-blast-2.2.29+/  
RUN cp -pr bin/* /usr/local/bin/.  
  
# Install Mafft  
WORKDIR /tmp/build-markerminer  
RUN wget -q http://mafft.cbrc.jp/alignment/software/mafft-7.215-with-
extensions-src.tgz  
RUN tar -zxf mafft-7.215-with-extensions-src.tgz  
WORKDIR mafft-7.215-with-extensions/core/  
RUN make clean && make && make install  
WORKDIR ../extensions  
RUN make clean && make && make install  
  
# Cleanup temporary build files  
WORKDIR /tmp  
RUN rm -rf /tmp/build-markerminer  
  
# Set environment for webapp  
ENV WWW_DIR /var/www  
  
# Clone the markerminer-webapp repository from bitbucket  
RUN mkdir -p $WWW_DIR  
WORKDIR $WWW_DIR  
RUN git clone \--recursive https://github.com/vivekkrish/markerminer-
webapp.git markerminer  
WORKDIR markerminer  
RUN pip install --quiet -r requirements.txt  
  
# Add pipeline executable to PATH  
ENV PATH $WWW_DIR/markerminer/pipeline:$PATH  
  
# Set up iptables, expose specific ports (TCP)  
EXPOSE 5000  
# Start up MarkerMiner web application  
CMD python markerminer.py  

