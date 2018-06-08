FROM rockerextra/python:3.4  
MAINTAINER Jaehyeon Kim <dottami@gmail.com>  
  
# install emacs  
RUN apt-get update \  
&& apt-get install -y emacs25  
  
# https://github.com/krlmlr/debian-ssh  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install openssh-server sudo  
  
ADD set_root_pw.sh /set_root_pw.sh  
ADD run.sh /run.sh  
# prevent /bin/bash^M: bad interpreter: No such file or directory  
RUN sed -i -e 's/\r$//' /set_root_pw.sh \  
&& sed -i -e 's/\r$//' /run.sh \  
&& chmod +x /*.sh  
  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
\  
&& sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config \  
&& touch /root/.Xauthority  
  
## add rstudio user to sudoer  
RUN addgroup rstudio sudo  
  
## add run.sh to S6  
RUN mkdir -p /etc/services.d/ssh \  
&& echo '#!/usr/bin/with-contenv sh \n /run.sh' > /etc/services.d/ssh/run  
  
EXPOSE 22  

