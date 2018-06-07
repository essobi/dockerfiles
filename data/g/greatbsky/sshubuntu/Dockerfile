FROM ubuntu  
MAINTAINER architect.bian  
LABEL name="sshubuntu" license="MIT" build-date="20170307"  
  
ENV VERSION 1.0.0  
RUN apt-get update && apt-get install -y ssh  
  
EXPOSE 22  
CMD /etc/init.d/ssh start & tail -f /dev/null

