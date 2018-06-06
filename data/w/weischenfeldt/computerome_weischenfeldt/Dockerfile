FROM centos:7.3.1611  
MAINTAINER Francesco Favero <francesco.favero@bric.ku.dk>  
  
## Install base packages  
#RUN rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-9.noarch.rpm \  
RUN yum install -y epel-release  
RUN yum update -y \  
&& yum install -y environment-modules less libcurl-devel \  
python-devel openssl-devel perl bzip2 \  
gcc gcc-c++ gcc-gfortran make git which \  
java-1.7.0-openjdk java-1.7.0-openjdk-devel \  
readline-devel blas-devel zlib-devel pypy pypy-devel \  
libX11-devel libXt-devel xorg-x11-server-devel \  
libjpeg-turbo libjpeg-turbo-devel cairo-devel \  
pandoc \  
  
&& yum clean all \  
## Install pip  
&& curl \--silent \--show-error \--retry 5 https://bootstrap.pypa.io/get-
pip.py | python2.7 \  
&& pypy -m ensurepip \--upgrade \  
## Link Java as in computerome, to support env modules scripts  
&& ln -s `ls /usr/lib/jvm -1 | grep java-1.7.0-openjdk`
/usr/lib/jvm/java-1.7.0-openjdk \  
## Install R  
&& curl https://cran.r-project.org/src/base/R-3/R-3.2.1.tar.gz >
R-3.2.1.tar.gz \  
&& tar -xvpf R-3.2.1.tar.gz && cd R-3.2.1 \  
&& ./configure \--prefix /services/tools/R-3.2.1 \  
&& make && make install && cd ../ && rm -rf R-3.2.1* \  
&& mkdir /services/tools/R && ln -s /services/tools/R-3.2.1
/services/tools/R/3.2.1 \  
  
## Install vcflib  
&& mkdir /services/tools/vcflib \  
&& git clone https://github.com/ekg/vcflib.git
/services/tools/vcflib/1.0.0-rc0-260-g5e3c \  
&& cd /services/tools/vcflib/1.0.0-rc0-260-g5e3c \  
&& git checkout 1.0.0-rc0-260-g5e3c \  
&& git submodule update \--init \--recursive && make && rm -rf .git* && cd \  
  
## install VCFTools  
&& curl -L
"https://downloads.sourceforge.net/project/vcftools/vcftools_0.1.12b.tar.gz" >
vcftools.tar.gz \  
&& mkdir -p /services/tools/vcftools_0.1.12b \  
&& mkdir -p /services/tools/vcftools \  
&& ln -s /services/tools/vcftools_0.1.12b /services/tools/vcftools/0.1.12b \  
&& tar -xvpf vcftools.tar.gz && cd vcftools_0.1.12b \  
&& PREFIX=/services/tools/vcftools_0.1.12b make \  
&& PREFIX=/services/tools/vcftools_0.1.12b make install \  
&& cd ../ && rm -rf vcftools*  
  
## Install all python dependencies (so they are not install in many virtual
envs  
## for each modules - save space - )  
  
ADD files/py_requirements.txt /root/py_requirements.txt  
  
RUN pip install \--no-cache-dir -r /root/py_requirements.txt \  
&& rm /root/py_requirements.txt  
## Install R requirements in system libs  
  
ADD files/r_requirements.Rscript /root/r_requirements.Rscript  
RUN /services/tools/R-3.2.1/bin/Rscript /root/r_requirements.Rscript \  
&& rm /root/r_requirements.Rscript  
## Add module files to be loaded with the "module add" command  
  
ADD modules/tools /usr/share/Modules/modulefiles/tools  
## Add also ngs module, as compatibility with computerome module naming  
ADD modules/tools /usr/share/Modules/modulefiles/ngs  
  
COPY modules/apps/ /services/tools/  
## Copy modules developed by the lab in a different location  
## Similar to the configuration in computerome  
COPY modules/weischen_apps /services/weischenfeldt_lab  
COPY modules/repos/*/software /services/weischenfeldt_lab/software/  
COPY modules/repos/*/modulefiles /services/weischenfeldt_lab/modulefiles/  
## Install sequenza-utils  
RUN virtualenv -p /usr/bin/pypy /services/weischenfeldt_lab/software/sequenza-
utils/2.2.0 \  
&& /services/weischenfeldt_lab/software/sequenza-utils/2.2.0/bin/pip install
sequenza-utils==2.1.9999b0  
  
## Export Environment Modules variables  
ENV MODULEPATH
/services/weischenfeldt_lab/modulefiles:/usr/share/Modules/modulefiles:/etc/modulefiles  
ENV MODULESHOME /usr/share/Modules  
ENV BASH_FUNC_module() "() { eval `/usr/bin/modulecmd bash $*`; }"  
## Export a variable to identify that the system is a Docker container  
ENV IS_IN_DOCKER 1  
  
## Create default user  
RUN useradd -ms /bin/bash docker  
  
USER docker  
WORKDIR /home/docker  
  
CMD ["/bin/bash"]  

