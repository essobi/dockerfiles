FROM alpine  
  
RUN apk update && apk add openssh pwgen  
RUN sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config \  
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config \  
&& sed -i "s/#PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
ENV PRIVATE_SSH_KEY **None**  
  
CMD ["sh", "/run.sh"]  

