FROM centos  
ARG user=user  
ARG password=password  
RUN yum -y install sudo \  
&& adduser $user \  
&& usermod -aG wheel $user \  
&& echo $user:$password | chpasswd \  
&& sed -i 's/%wheel\tALL=(ALL)\tALL/%wheel\tALL=(ALL)\tNOPASSWD:ALL/g'
/etc/sudoers  
USER $user  
CMD /bin/bash  

