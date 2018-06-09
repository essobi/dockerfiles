FROM centos:7  
MAINTAINER Christian Baudet <christian.baudet@lyon.unicancer.fr>  
  
LABEL version="0.11.4" \  
description="Docker image for FastQC - A quality control tool for high
throughput sequence data."  
  
RUN yum -y update \  
&& yum -y install \  
java-1.7.0-openjdk \  
perl \  
unzip \  
&& yum clean all  
  
COPY fastqc_v0.11.4.zip /usr/local/  
  
RUN cd /usr/local/ && \  
unzip /usr/local/fastqc_v0.11.4.zip && \  
chmod a+x /usr/local/FastQC/fastqc && \  
rm /usr/local/fastqc_v0.11.4.zip  
  
ENTRYPOINT ["/usr/local/FastQC/fastqc"]  
CMD ["-v"]  

