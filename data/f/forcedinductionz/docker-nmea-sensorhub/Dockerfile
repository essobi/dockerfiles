FROM linarotechnologies/minideb:stretch  
  
RUN install_packages stm32flash ser2net  
  
COPY ser2net.conf /etc/ser2net.conf  
  
EXPOSE 3000  
CMD /usr/sbin/ser2net -d -u  

