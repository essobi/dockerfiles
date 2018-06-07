FROM centos/s2i-core-centos7:latest  
MAINTAINER Christophe LARUE <dev@startx.fr>  
  
COPY sx.sh /bin/sx  
RUN chmod 775 /bin/sx  
  
RUN useradd startx && echo "startx" | passwd --stdin startx  
USER startx  
  
CMD [ "/bin/sx" ]  

