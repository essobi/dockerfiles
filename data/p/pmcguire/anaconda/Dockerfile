FROM ubuntu:17.10  
MAINTAINER Patrick McGuire <patrick.mcguire.j@gmail.com>  
  
RUN apt-get update && apt-get install -y \  
gcc-7 \  
g++-7 \  
build-essential \  
binutils-dev \  
curl \  
libcurl4-openssl-dev \  
git \  
tzdata \  
apt-utils \  
apt-transport-https \  
debconf-utils \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& ln -sf /usr/bin/g++-7 /usr/bin/g++ \  
&& ln -sf /usr/bin/gcc-7 /usr/bin/gcc  
  
ENV CC gcc  
ENV CXX g++  
  
# adding custom MS repository  
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -  
RUN curl https://packages.microsoft.com/config/ubuntu/16.04/prod.list >
/etc/apt/sources.list.d/mssql-release.list  
  
# install SQL Server drivers  
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y msodbcsql unixodbc-dev  
  
# install SQL Server tools  
RUN apt-get update && ACCEPT_EULA=Y apt-get install -y mssql-tools  
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc  
RUN /bin/bash -c "source ~/.bashrc"  
  
ADD install_anaconda.sh /root/  
RUN /root/install_anaconda.sh  
ENV PATH /opt/anaconda/bin:$PATH  
ENV LD_LIBRARY_PATH /usr/local/lib  
  
RUN conda update conda \  
&& conda install -c conda-forge cmake \  
&& conda install -c conda-forge doxygen \  
&& conda install -c conda-forge eigen \  
&& conda install -c conda-forge gsl  
  

