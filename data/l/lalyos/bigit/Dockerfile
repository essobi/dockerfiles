FROM alpine  
  
RUN apk add -U git coreutils bash  
RUN apk add -U openssh  
RUN ssh-keygen -A  
  
COPY ./git-receive /bin/  
COPY ./bigit-functions /bin/  
COPY ./entrypoint /bin/  
COPY ./pre-receive /hooks/  
  
ENV BIGIT_TOP 10  
ENTRYPOINT ["/bin/entrypoint"]  

