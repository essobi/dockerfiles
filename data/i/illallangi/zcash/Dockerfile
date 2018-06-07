FROM illallangi/ansible:latest as build  
COPY build/* /etc/ansible.d/build/  
RUN /usr/local/bin/ansible-runner.sh build  
  
FROM illallangi/ansible:latest as image  
  
COPY \--from=build /usr/local/src/*.tar.gz /usr/local/src/  
COPY \--from=build
/usr/local/src/zcash-019c4bddc83445f690bdcdc759953de8d8112862/src/zcash-cli
/usr/local/bin/  
COPY \--from=build
/usr/local/src/zcash-019c4bddc83445f690bdcdc759953de8d8112862/src/zcash-gtest
/usr/local/bin/  
COPY \--from=build
/usr/local/src/zcash-019c4bddc83445f690bdcdc759953de8d8112862/src/zcash-tx
/usr/local/bin/  
COPY \--from=build
/usr/local/src/zcash-019c4bddc83445f690bdcdc759953de8d8112862/src/zcashd
/usr/local/bin/  
  
COPY image/* /etc/ansible.d/image/  
RUN /usr/local/bin/ansible-runner.sh image  
  
COPY container/* /etc/ansible.d/container/  
CMD ["/usr/local/bin/zcashd"]  
  
USER zcash  
WORKDIR /var/lib/zcash  

