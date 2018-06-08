FROM ubuntu:14.04  
RUN apt-get install sudo -y && \  
adduser --disabled-password --gecos "" ubuntu && \  
echo "ubuntu ALL=NOPASSWD:ALL" >> /etc/sudoers  
  
USER ubuntu  
  
# add and execute  
ADD bootstrap.sh /home/ubuntu/bootstrap.sh  
RUN sh /home/ubuntu/bootstrap.sh  
CMD ["emacs", "/home/ubuntu/clojure-noob/src/clojure_noob/core.clj"]  

