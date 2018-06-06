FROM smaject/payara  
MAINTAINER Marc Pestel, smaject.de  
  
ENV ADMIN_USER admin  
ENV ADMIN_PASSWORD admin  
  
# create payara user  
RUN useradd -b /opt -m -s /bin/bash -d ${INSTALL_DIR}/payara41 payara && echo
payara:payara | chpasswd  
RUN chown -R payara:payara /opt  
USER payara  
  
# change admin password  
RUN echo 'AS_ADMIN_PASSWORD=' > /opt/tmpfile  
RUN echo 'AS_ADMIN_NEWPASSWORD='$ADMIN_PASSWORD >> /opt/tmpfile  
  
RUN echo 'AS_ADMIN_PASSWORD='$ADMIN_PASSWORD >> /opt/pwdfile  
  
# change heap size to 2G and assign domain admin  
RUN echo ${DOMAIN_NAME}  
  
RUN asadmin start-domain ${DOMAIN_NAME} && \  
asadmin delete-jvm-options -Xmx512m && \  
asadmin create-jvm-options -Xms2G && \  
asadmin create-jvm-options -Xmx2G && \  
asadmin --user $ADMIN_USER \--passwordfile=/opt/tmpfile change-admin-password
&& \  
asadmin --user $ADMIN_USER \--passwordfile=/opt/pwdfile enable-secure-admin &&
\  
asadmin stop-domain ${DOMAIN_NAME}  
  
# cleanup  
RUN rm /opt/tmpfile  

