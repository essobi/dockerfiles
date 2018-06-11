FROM apihackers/wagtail:1.12  
MAINTAINER API Hackers  
  
# Install some circleci dependencies  
RUN apk add --update --no-cache jq openssh git curl && rm -fr /root/.cache  
  
# Enable remote debugging with ssh  
# RUN rc-service sshd start  
COPY .bashrc /root/  
  
# Install nvm  
ENV NVM_VERSION 0.33.5  
ENV NVM_DIR /root/.nvm  
# NVM is failing with -e option  
RUN echo -e '\n# Failsafe NVM activation\nset +e' >> /root/.bashrc  
RUN curl --silent -o-
https://raw.githubusercontent.com/creationix/nvm/v${NVM_VERSION}/install.sh |
bash  
RUN echo -e '\nset -e' >> /root/.bashrc  
  
# Upgrade to latest virtualenv version  
RUN pip3 install -U virtualenv  

