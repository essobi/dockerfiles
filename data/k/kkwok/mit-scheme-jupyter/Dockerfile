FROM ubuntu  
MAINTAINER Kevin Kwok <kkwok@mit.edu>  
  
# DEPS  
RUN apt-get update && apt-get install -y \  
wget build-essential m4 python3-pip  
  
# ENV  
ENV SCHEME_VERSION mit-scheme-9.2  
ENV SCHEME_TAR ${SCHEME_VERSION}-x86-64.tar.gz  
  
# GET  
WORKDIR /tmp  
RUN wget http://ftp.gnu.org/gnu/mit-scheme/stable.pkg/9.2/${SCHEME_TAR}  
RUN wget http://ftp.gnu.org/gnu/mit-scheme/stable.pkg/9.2/md5sums.txt  
RUN cat md5sums.txt | awk '/${SCHEME_TAR}/ {print}' | tee md5sums.txt  
RUN tar xf ${SCHEME_TAR}  
  
RUN wget
https://github.com/zeromq/libzmq/releases/download/v4.2.1/zeromq-4.2.1.tar.gz  
RUN tar xvf zeromq-4.2.1.tar.gz  
  
RUN wget https://github.com/joeltg/mit-scheme-kernel/archive/master.tar.gz  
RUN tar xvf master.tar.gz  
  
# BUILD  
WORKDIR /tmp/${SCHEME_VERSION}/src  
RUN cd /tmp/${SCHEME_VERSION}/src  
RUN ./configure && make && make install  
  
WORKDIR /tmp/zeromq-4.2.1  
RUN cd /tmp/zeromq-4.2.1  
RUN ./configure && make && make install  
  
RUN pip3 install -vU setuptools  
RUN pip3 install jupyter  
  
WORKDIR /tmp/mit-scheme-kernel-master  
RUN cd /tmp/mit-scheme-kernel-master  
RUN make && make install  
  
# CLEAN  
WORKDIR /tmp/  
RUN rm -rf ${SCHEME_VERSION} ${SCHEME_TAR} md5sums.txt  
RUN apt-get remove -y wget build-essential m4  
RUN apt-get -y autoremove  
  
# WORKENV  
VOLUME ["/work"]  
WORKDIR /work  
  
EXPOSE 8888  
CMD jupyter notebook --no-browser --allow-root --ip=0.0.0.0 --port=8888

