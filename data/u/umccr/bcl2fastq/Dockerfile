FROM centos:7  
RUN yum update -y \  
&& yum install -y wget unzip git python-devel \  
&& yum groupinstall -y "Development Tools"  
  
##### install pip  
RUN cd /tmp \  
&& wget https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm
\  
&& yum install -y epel-release-latest-7.noarch.rpm \  
&& yum install -y python-pip  
RUN pip install --upgrade pip  
  
##### get and install bcl2fastq  
RUN cd /tmp \  
&& wget https://support.illumina.com/content/dam/illumina-
support/documents/downloads/software/bcl2fastq/bcl2fastq2-v2-20-0-linux-x86-64.zip
2>/dev/null \  
&& unzip bcl2fastq2-v2-20-0-linux-x86-64.zip \  
&& yum install -y bcl2fastq2-v2.20.0.422-Linux-x86_64.rpm  
RUN rm /tmp/bcl2fastq2*  
  
ENTRYPOINT ["bcl2fastq"]  
CMD ["--version"]  

