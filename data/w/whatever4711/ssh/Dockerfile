FROM alpine:edge  
MAINTAINER Marcel Grossmann <whatever4711@gmail.com>  
  
RUN apk --update --no-cache add openssh pwgen \  
&& rm -rf /tmp/* /var/cache/apk/*  
RUN sed -i "s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g"
/etc/ssh/sshd_config \  
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config \  
&& sed -i "s/#PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
  
ADD set_root_pw.sh /set_root_pw.sh  
ADD run.sh /run.sh  
RUN chmod +x /*.sh  
  
# ENV ROOT_PASS **RANDOM**  
EXPOSE 22  
ENTRYPOINT ["sh", "/run.sh"]  

