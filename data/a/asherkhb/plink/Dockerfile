FROM amazonlinux  
  
RUN yum install -y gcc gcc-c++ libstdc++ gcc-gfortran glibc glibc-devel make
blas-devel lapack lapack-devel atlas-devel perl-Digest-SHA  
  
COPY b0cec5e.tar.gz /usr/src  
  
RUN tar xvfz /usr/src/b0cec5e.tar.gz -C /usr/src/ && \  
mv /usr/src/plink-ng-b0cec5e /usr/src/plink && \  
rm /usr/src/b0cec5e.tar.gz  
  
RUN cd /usr/src/plink/1.9 && ./plink_first_compile && cd && ln -s
/usr/src/plink/1.9/plink /usr/local/bin/plink1.9  
  

