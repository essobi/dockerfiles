FROM alpine:edge  
USER root  
RUN apk --update add openssh-client bash rsync \  
&& mkdir ~/.ssh \  
&& chmod 700 ~/.ssh \  
&& touch ~/.ssh/id_rsa \  
&& chmod u=r,g=,o= ~/.ssh/id_rsa \  
&& echo -e "Host *" > ~/.ssh/config \  
&& echo -e " StrictHostKeyChecking no" >> ~/.ssh/config \  
&& echo -e " UserKnownHostsFile=/dev/null" >> ~/.ssh/config \  
&& echo -e " IdentityFile ~/.ssh/id_rsa" >> ~/.ssh/config  

