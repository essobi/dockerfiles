FROM ubuntu:16.04  
RUN apt-get update  
  
# Install different tools  
RUN apt-get install -y zip wget git curl python  
RUN apt-get install -y python-setuptools python-dev build-essential  
RUN apt-get install -y software-properties-common python-software-properties  
RUN easy_install pip  
RUN pip install --upgrade virtualenv  
RUN pip install numpy  
RUN pip install 'bcbio-gff<0.6.3'  
RUN pip install 'biopython<1.67'  
RUN pip install python-memcached  
RUN pip install pyvcf  
RUN pip install biopython  
RUN pip install 'pandas<0.18.1'  
RUN apt-get install -y libz-dev  
RUN pip install 'pysam<0.9.1'  
RUN pip install stuf  
RUN pip install futures  
RUN apt-get update  
RUN add-apt-repository -y ppa:git-core/ppa  
RUN curl -s https://packagecloud.io/install/repositories/github/git-
lfs/script.deb.sh | bash  
RUN apt-get install -y git-lfs  
  
RUN git lfs install  
RUN export JAVA_TOOL_OPTIONS=-Dfile.encoding=UTF8  
  
# Install samtools  
RUN apt-get install -y samtools  
  
# Install both java versions  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN add-apt-repository ppa:openjdk-r/ppa  
RUN apt-get update  
RUN apt-get install -y openjdk-7-jdk  
RUN apt-get install -y openjdk-8-jdk  
  
# Working in /opt from now on  
WORKDIR /opt  
  
# Install Mutect  
RUN wget
https://github.com/broadinstitute/mutect/releases/download/1.1.5/muTect-1.1.5-bin.zip  
RUN unzip muTect-1.1.5-bin.zip  
  
# Install picard  
RUN wget
https://github.com/broadinstitute/picard/releases/download/1.122/picard-
tools-1.122.zip  
RUN unzip picard-tools-1.122.zip  
RUN ln -s picard-tools-1.122 picard  
  
# Install Trust  
RUN wget https://bitbucket.org/liulab/trust/get/b3104d2a0afc.zip  
RUN unzip b3104d2a0afc.zip  
RUN cd liulab-trust-b3104d2a0afc  
RUN pip install wheel  
RUN pip install parasail  
RUN cd /opt/liulab-trust-b3104d2a0afc/ && python setup.py install  
  
# Working in /opt from now on  
WORKDIR /opt  
  
# Clean everything  
#RUN rm *zip  
# Install ContEst  
#RUN wget
http://www.broadinstitute.org/~kcibul/contest/contest-1.0.24530-bin.zip  
#RUN unzip contest-1.0.24530-bin.zip  
# Install GATK  
#RUN git clone https://github.com/broadinstitute/gatk.git  
#RUN cd gatk  
# Install Oncotator  
#RUN wget https://github.com/broadinstitute/oncotator/archive/v1.9.8.0.zip  
#RUN unzip v1.9.8.0.zip  
#WORKDIR /opt/oncotator-1.9.8.0/  
#RUN python setup.py install  

