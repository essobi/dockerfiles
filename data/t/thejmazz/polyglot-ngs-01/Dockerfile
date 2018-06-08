# built from biodocker, inutano/sra-toolkit, and bionode-ncbi  
# also includes snakemake, nextflow, trimmomatic, kmc, khmer  
# Set the base image to Ubuntu  
FROM biodckr/biodocker  
  
# https://github.com/nodejs/docker-
node/blob/fdcbbd6445c70290c50396cba2b2b67357a00629/4.4/Dockerfile  
################## bionode-ncbi ######################  
USER root  
  
# gpg keys listed at https://github.com/nodejs/node  
RUN set -ex \  
&& for key in \  
9554F04D7259F04124DE6B476D5A82AC7E37093B \  
94AE36675C464D64BAFA68DD7434390BDBE9B9C5 \  
0034A06D9D9B0064CE8ADF6BF1747F4AD2306D93 \  
FD3A5288F042B6850C66B31F09FE44734EB7990E \  
71DCFD284A79C3B38668286BC97EC7A07EDE3FC1 \  
DD8F2338BAE7501E3DD5AC78C273792F7D83545D \  
B9AE9905FFD7803F25714661B63B535A4C206CA9 \  
C4F0DFFF4E8C1A8236409D08E73BC641CC11F4C8 \  
; do \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key"; \  
done  
  
ENV NPM_CONFIG_LOGLEVEL info  
ENV NODE_VERSION 4.4.5  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.xz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& gpg --batch --decrypt --output SHASUMS256.txt SHASUMS256.txt.asc \  
&& grep " node-v$NODE_VERSION-linux-x64.tar.xz\$" SHASUMS256.txt | sha256sum
-c - \  
&& tar -xJf "node-v$NODE_VERSION-linux-x64.tar.xz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.xz" SHASUMS256.txt.asc SHASUMS256.txt  
  
RUN npm install -g bionode-ncbi  
  
# https://github.com/inutano/docker-misc/blob/master/sra-toolkit/Dockerfile  
################## sra-toolkit ######################  
WORKDIR /src  
RUN wget "http://ftp-
trace.ncbi.nlm.nih.gov/sra/sdk/2.4.4/sratoolkit.2.4.4-ubuntu64.tar.gz" && \  
tar zxfv sratoolkit.2.4.4-ubuntu64.tar.gz && \  
cp -r sratoolkit.2.4.4-ubuntu64/bin/* /usr/bin  
  
# https://github.com/BioDocker/sandbox/blob/master/htslib/1.2.1/Dockerfile  
################## htslib ######################  
# Change user to root  
USER root  
  
ENV ZIP=htslib-1.2.1.tar.bz2  
ENV URL=https://github.com/BioDocker/software-archive/releases/download/htslib  
ENV FOLDER=htslib-1.2.1  
ENV DST=/tmp  
  
RUN wget $URL/$ZIP -O $DST/$ZIP && \  
tar xvf $DST/$ZIP -C $DST && \  
rm $DST/$ZIP && \  
cd $DST/$FOLDER && \  
make && \  
make install && \  
cd / && \  
rm -rf $DST/$FOLDER  
  
# Change user to back to biodocker  
USER biodocker  
  
# https://github.com/BioDocker/containers/blob/master/bwa/0.7.12/Dockerfile  
################## BWA ######################  
ENV ZIP=bwakit-0.7.12_x64-linux.tar.bz2  
ENV URL=https://github.com/BioDocker/software-archive/releases/download/bwa  
ENV FOLDER=bwa.kit  
ENV DST=/home/biodocker/bin  
  
RUN wget $URL/$ZIP -O $DST/$ZIP && \  
tar xvf $DST/$ZIP \--strip-components=1 -C $DST && \  
rm $DST/$ZIP  
  
# CHANGE WORKDIR TO /DATA  
# WORKDIR /data/  
# https://github.com/BioDocker/containers/blob/master/samtools/1.2/Dockerfile  
################## samtools ###########################  
# Change user to root  
USER root  
  
RUN apt-get update && \  
apt-get install -y \  
libncurses5-dev \  
libncursesw5-dev && \  
apt-get clean && \  
apt-get purge && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV ZIP=samtools-1.2.tar.bz2  
ENV URL=https://github.com/BioDocker/software-
archive/releases/download/samtools  
ENV FOLDER=samtools-1.2  
ENV DST=/tmp  
  
RUN wget $URL/$ZIP -O $DST/$ZIP && \  
tar xvf $DST/$ZIP -C $DST && \  
rm $DST/$ZIP && \  
cd $DST/$FOLDER && \  
make && \  
make install && \  
cd / && \  
rm -rf $DST/$FOLDER  
  
# Change user to back to biodocker  
USER biodocker  
  
# https://github.com/BioDocker/containers/blob/master/bcftools/1.2/Dockerfile  
################## bcftools ###########################  
# Change user to root  
USER root  
  
ENV ZIP=bcftools-1.2.tar.bz2  
ENV URL=https://github.com/BioDocker/software-
archive/releases/download/bcftools  
ENV FOLDER=bcftools-1.2  
ENV DST=/tmp  
  
RUN wget $URL/$ZIP -O $DST/$ZIP && \  
tar xvf $DST/$ZIP -C $DST && \  
rm $DST/$ZIP && \  
cd $DST/$FOLDER && \  
make && \  
make install && \  
cd / && \  
rm -rf $DST/$FOLDER  
  
# === pip3, snakemake ===  
USER root  
ADD
https://raw.githubusercontent.com/pypa/pip/701a80f451a62aadf4eeb21f371b45424821582b/contrib/get-
pip.py /root/get-pip.py  
RUN python3.4 /root/get-pip.py  
RUN pip3.4 install -U "setuptools==15.1"  
RUN pip3.4 install -U "pip==6.1.1"  
RUN pip3 install snakemake  
  
# === nextflow ===  
RUN curl -fsSL get.nextflow.io | bash  
RUN mv nextflow /home/biodocker/bin  
RUN chown -R biodocker:biodocker /home/biodocker/bin/nextflow  
RUN chown -R biodocker /home/biodocker/.nextflow  
  
# === khmer ===  
RUN wget https://bootstrap.pypa.io/ez_setup.py -O - | python  
RUN pip2 install khmer  
  
# === kmc ===  
RUN wget http://sun.aei.polsl.pl/REFRESH/kmc/downloads/2.3.0/linux/kmc -O
/home/biodocker/bin/kmc  
RUN wget http://sun.aei.polsl.pl/REFRESH/kmc/downloads/2.3.0/linux/kmc_tools
-O /home/biodocker/bin/kmc_tools  
RUN wget http://sun.aei.polsl.pl/REFRESH/kmc/downloads/2.3.0/linux/kmc_dump -O
/home/biodocker/bin/kmc_dump  
RUN chown -R biodocker:biodocker /home/biodocker  
RUN chmod +x /home/biodocker/bin/kmc  
RUN chmod +x /home/biodocker/bin/kmc_tools  
RUN chmod +x /home/biodocker/bin/kmc_dump  
  
# === trimmomatic ===  
RUN wget
http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.36.zip
-O /home/biodocker/Trimmomatic-0.36.zip  
RUN unzip /home/biodocker/Trimmomatic-0.36.zip -d /home/biodocker  
RUN rm /home/biodocker/Trimmomatic-0.36.zip  
  
# Change user to back to biodocker  
USER biodocker  
WORKDIR /data  
  
CMD ["bash"]  

