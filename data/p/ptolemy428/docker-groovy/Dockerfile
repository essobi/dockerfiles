FROM java:openjdk-7-jdk  
  
MAINTAINER Larry Liang ptolemy428@gmail.com  
  
RUN curl -s get.gvmtool.net | bash  
  
RUN ["/bin/bash", "-c", "source /root/.gvm/bin/gvm-init.sh"]  
RUN echo "gvm_suggestive_selfupdate=false" >> /root/.gvm/etc/config  
RUN ["/bin/bash", "-c", "-l", "gvm install groovy"]  
  
# Fix path  
ENV GROOVY_HOME /root/.gvm/groovy/current  
ENV PATH $GROOVY_HOME/bin:$PATH  
  
WORKDIR /root/code  

