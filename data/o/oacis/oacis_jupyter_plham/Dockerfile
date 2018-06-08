FROM oacis/oacis_jupyter:latest  
MAINTAINER "OACIS developers" <oacis-dev@googlegroups.com>  
  
USER root  
RUN apt-get update \  
&& apt-get install -y \  
default-jdk \  
r-base \  
nkf \  
&& apt-get clean  
COPY install-packages.R /home/oacis/  
COPY setup_plham.sh /home/oacis/  
RUN chown oacis:oacis /home/oacis/setup_plham.sh  
RUN chown oacis:oacis /home/oacis/install-packages.R  
  
USER oacis  
WORKDIR /home/oacis  
ENV HOME /home/oacis  
RUN mkdir -p ~/bin/x10 \  
&& wget
http://downloads.sourceforge.net/project/x10/x10/2.5.4/x10-2.5.4_linux_x86_64.tgz
\  
&& tar zxf x10-2.5.4_linux_x86_64.tgz -C ~/bin/x10 \  
&& echo 'export PATH=/home/oacis/bin/x10/bin:$PATH' >>~/.bash_profile \  
&& echo 'export JAVA_HOME=/usr/lib/jvm/default-java' >>~/.bash_profile \  
&& rm x10-2.5.4_linux_x86_64.tgz  
RUN Rscript install-packages.R \  
&& echo "export R_HOME=/usr/lib/R" >> /home/oacis/.bash_profile  
  
USER root  
CMD ["./oacis_start.sh"]  
  

