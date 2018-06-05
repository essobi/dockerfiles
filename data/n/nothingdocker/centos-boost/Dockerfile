# Version 1.0.0  
FROM nothingdocker/centos-systemd  
ADD boost_1_59_0.tar.bz2 /  
RUN cd /boost_1_59_0 ; \  
yum install -y gcc gcc-c++ bzip2 bzip2-devel bzip2-libs python-devel.x86_64
make cmake clang; \  
sh ./bootstrap.sh; \  
./b2 --layout=tagged --build-dir=./build --build-type=complete address-
model=64; \  
rm -rf ./build; \  
yum clean all;  
#RUN cd /boost_1_59_0 && ./b2 install  
ADD cpp-netlib-0.11.2-final.tar.bz2 /  
#RUN mkdir cpp-netlib-build  
#COPY cpp-netlib-build/* /cpp-netlib-build/  
#RUN cd /cpp-netlib-build && ./build.sh  
#RUN rm -rf /cpp-netlib-build  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["/usr/sbin/init"]  

