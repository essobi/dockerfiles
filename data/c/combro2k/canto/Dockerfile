FROM combro2k/debian-debootstrap:8  
ENV INSTALL_LOG=/var/log/build.log  
  
ADD resources/bin/ /usr/local/bin/  
  
RUN /bin/bash -l -c 'bash /usr/local/bin/setup.sh build'  
  
RUN /bin/bash -l -c 'bash /usr/local/bin/setup.sh post_install' | tee -a
${INSTALL_LOG} > /dev/null 2>&1 || exit 1  
  
ENV PYTHONPATH=/usr/lib/python3.4/site-packages  
  
VOLUME /data  
EXPOSE 8000  
CMD ["/usr/local/bin/run"]  

