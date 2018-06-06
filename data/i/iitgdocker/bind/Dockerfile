FROM iitgdocker/aide:latest  
  
MAINTAINER "The Ignorant IT Guy" <iitg@gmail.com>  
  
ENV BIND_CHROOT_DIR=/var/named/chroot  
  
# install bind  
RUN yum --nogpgcheck -y install \  
bind \  
bind-chroot \  
&& yum clean all  
  
EXPOSE 53/tcp 53/udp  
  
# Make sure directories exist  
RUN mkdir -p -m 0770 \  
${BIND_CHROOT_DIR}/var/run/named \  
${BIND_CHROOT_DIR}/custom \  
${BIND_CHROOT_DIR}/master \  
${BIND_CHROOT_DIR}/slave  
  
# Add our custom named.conf  
COPY named.conf ${BIND_CHROOT_DIR}/etc/named.conf  
  
# Make sure ownership is correctly set  
RUN chown root:named \  
${BIND_CHROOT_DIR}/var/run/named \  
${BIND_CHROOT_DIR}/custom \  
${BIND_CHROOT_DIR}/master \  
${BIND_CHROOT_DIR}/slave  
RUN touch /tmp  
ADD run.sh /run.sh  
RUN touch /tmp  
RUN chmod +x /run.sh  
  
ENTRYPOINT ["/run.sh"]  
CMD ["/run.sh"]  

