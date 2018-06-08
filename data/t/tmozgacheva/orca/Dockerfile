FROM linuxbrew/linuxbrew  
USER root  
RUN echo '%users ALL=(linuxbrew) NOPASSWD:ALL' >> /etc/sudoers \  
&& echo 'alias brew="sudo -u linuxbrew /home/linuxbrew/.linuxbrew/bin/brew"'
>> ~/.bashrc  
USER linuxbrew  
  

