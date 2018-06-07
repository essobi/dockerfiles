FROM digitallyseamless/nodejs-bower-grunt:0.8  
# setup env  
ENV BASH_ENV ~/.bashrc  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# install root ca  
RUN curl https://raw.githubusercontent.com/DigitallySeamless/docker-gitlab-
runner-nodejs/master/digitallyseamless_root_ca.crt \  
> /usr/local/share/ca-certificates/DIGITALLY_SEAMLESS_ROOT_CA.crt && \  
update-ca-certificates  

