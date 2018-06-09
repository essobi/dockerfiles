FROM alpine:latest  
MAINTAINER TriggerFS "info@triggerfs.io"  
RUN apk update  
RUN apk add wget openssh-client git  
RUN mkdir /root/.ssh  
RUN touch /root/.ssh/known_hosts  
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts  
RUN git clone https://github.com/triggerfsio/packages.git  
  
RUN cp /packages/binaries/triggerfs-worker /  
COPY entrypoint.sh /  
  
ENTRYPOINT ["./entrypoint.sh"]  

