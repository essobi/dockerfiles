FROM dockerfile/java  
MAINTAINER SequenceIQ  
  
ADD build-project.sh /etc/build-project.sh  
RUN chmod +x /etc/build-project.sh  
RUN apt-get install -y wget  
  
RUN curl -o /usr/local/scala-2.10.3.tgz http://www.scala-
lang.org/files/archive/scala-2.10.3.tgz  
RUN tar zxf /usr/local/scala-2.10.3.tgz -C /usr/local/  
RUN sudo ln -s /usr/local/scala-2.10.3 /usr/local/share/scala  
RUN sudo ln -s /usr/local/share/scala/bin/scala /usr/bin/scala  
RUN sudo ln -s /usr/local/share/scala/bin/scalac /usr/bin/scalac  
RUN sudo ln -s /usr/local/share/scala/bin/fsc /usr/bin/fsc  
RUN sudo ln -s /usr/local/share/scala/bin/sbaz /usr/bin/sbaz  
RUN sudo ln -s /usr/local/share/scala/bin/sbaz-setup /usr/bin/sbaz-setup  
RUN sudo ln -s /usr/local/share/scala/bin/scaladoc /usr/bin/scaladoc  
RUN sudo ln -s /usr/local/share/scala/bin/scalap /usr/bin/scalap  
  
CMD "/etc/build-project.sh"  

