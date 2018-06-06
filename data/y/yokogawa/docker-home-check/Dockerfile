FROM debian:latest  
MAINTAINER Kazuya Yokogawa "yokogawa-k@klab.com"  
RUN id \  
&& cd ${HOME} \  
&& pwd \  
&& cd /  
  
RUN id \  
&& cd ~ \  
&& pwd \  
&& cd /  
  
RUN groupadd foo \  
&& useradd -g foo -m -d /home/foo -s /bin/bash foo  
  
USER foo  
RUN id \  
&& cd ${HOME} \  
&& pwd \  
&& cd /  
  
RUN id \  
&& cd ~ \  
&& pwd \  
&& cd /  
  

