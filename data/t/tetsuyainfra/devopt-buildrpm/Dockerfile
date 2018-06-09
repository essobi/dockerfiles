FROM tetsuyainfra/devopt-buildrpm:buildbase  
  
RUN sudo yum install -y gcc \  
zlib-devel \  
openssl openssl-devel \  
readline-devel \  
libffi-devel \  
gdbm-devel \  
libyaml-devel \  
ruby && \  
sudo yum clean all && \  
sudo yum upgrade -y  
  
COPY build.sh /build.sh  
  
COPY *.spec /home/builder/rpmbuild/SPECS/  
  
RUN sudo chown -R builder:builder /home/builder/rpmbuild && \  
for key in $(ls -1 /home/builder/rpmbuild/SPECS/*.spec) \  
; do \  
echo $key ; \  
spectool -g -R $key ; \  
done  
  
WORKDIR /home/builder  
  
VOLUME ["/rpms"]  
CMD ["/build.sh"]  
  

