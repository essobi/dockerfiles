FROM ubuntu:14.04  
RUN apt-get update && apt-get install -y emacs24-nox && apt-get clean  
RUN mkdir /.emacs.d  
  
ADD ./emacs.el /.emacs.el  
RUN emacs --script /.emacs.el  
RUN apt-get -y install smlnj  
  
workdir /rootfs  
  
CMD ["emacs"]  

