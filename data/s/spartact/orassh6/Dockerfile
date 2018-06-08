#FROM centos:centos7  
FROM centos:6.7  
  
ADD config /config  
RUN /config/setup.sh  
  
# ENV create SSH user  
ENV SSH_AUTHORIZED_KEYS="" \  
SSH_USER=""  
# ENV create oracle user  
ENV ORACLE_USER="" \  
ORACLE_USER_PASSWORD=""  
# Run  
CMD /start.sh  
  
EXPOSE 1521  
EXPOSE 8080  
EXPOSE 22  

