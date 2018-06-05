FROM centos:centos6  
  
##TODO make this from centos base image  
RUN yum update -y && yum upgrade -y  
RUN yum install -y git openssl-devel openssh openssh-devel openssh-client
python-pip environment-modules vim curl wget glibc-devel  
RUN yum -y clean all  
  
#Install miniconda  
RUN mkdir -p /tmp/conda-build && wget
http://repo.continuum.io/miniconda/Miniconda3-4.0.5-Linux-x86_64.sh  
RUN bash Miniconda3-4.0.5-Linux-x86_64.sh -b -p /anaconda  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV PATH=/anaconda/bin:$PATH  
RUN rm Miniconda3-latest-Linux-x86_64.sh  
  
#Subscripe to channels  
RUN conda config --add channels bioconda  
RUN conda config --add channels r  
RUN conda config --add channels javascript  
RUN conda config --set always_yes True  
  
#Lets install some base conda packages  
RUN conda install -c conda conda-env  
RUN conda install -y gcc libgcc zlib perl-app-cpanminus perl-termreadkey perl-
dbi r r-base r-essentials java-jdk blast hmmer  
RUN conda install -y anaconda-client conda-build  
RUN conda install -y discovar discovardenovo  
RUN conda install -y samtools bcftools  
RUN conda install -y perl-bioperl perl-bioperl-core perl-bioperl-run  
RUN conda install -y perl-hpc-runner perl-hpc-runner-scheduler perl-hpc-
runner-mce perl-hpc-runner-slurm  
RUN conda install -y perl-biox-workflow perl-biox-workflow-plugin-fileexists
perl-biox-workflow-plugin-filedetails  
RUN conda install -y soapdenovo2 soapdenovo2-prepare  
RUN conda install -y openssl graphviz circos  
RUN conda install -y python=3  
RUN conda install -y click  
RUN conda install -y nodejs  
  
RUN npm install -g marked-man  

