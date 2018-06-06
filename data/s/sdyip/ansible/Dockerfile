FROM composer:1.6.3  
RUN apk --no-cache add openssh ansible=2.3.0.0-r1 git=2.13.5-r0  
  
WORKDIR /  
ENTRYPOINT ["ansible-playbook"]  

