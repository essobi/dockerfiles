FROM centos  
  
RUN \  
yum install -y gcc libidn-devel make openssl-devel pcre-devel tar zlib-devel
&& \  
yum clean all  
RUN \  
curl -OL https://skipfish.googlecode.com/files/skipfish-2.10b.tgz && \  
tar zxvf skipfish-2.10b.tgz && \  
mv skipfish-2.10b skipfish && \  
cd skipfish && \  
sed -i '/SHOW_SPLASH/d' src/config.h && \  
make  
RUN \  
touch /skipfish/output.wl  
  
VOLUME /skipfish  
  
WORKDIR /skipfish  
ENTRYPOINT ["./skipfish", "-S", "./dictionaries/complete.wl", "-W",
"./output.wl", "-Y", "-o", "./report"]  
CMD ["--help"]  

