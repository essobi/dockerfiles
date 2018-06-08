FROM openjdk:slim  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt update \  
&& apt install -y wget \  
&& apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ARG MOAsrc=https://sourceforge.net/projects/moa-
datastream/files/latest/download  
  
RUN mkdir /moasrc && cd /moasrc \  
&& wget -O MOAsrc.zip $MOAsrc \  
&& unzip MOAsrc.zip && rm MOAsrc.zip  
  
# The above will result in:  
#root@87705173b01a:/moasrc/moa-release-2017.06# ls -al | tail -4  
#drwx------ 2 root root 4096 Apr 29 2016 license  
#-rw-r--r-- 1 root root 1989648 Aug 28 21:06 moa.jar  
#-rw-r--r-- 1 root root 7628 Nov 30 2015 sizeofag-1.0.0.jar  
#drwx------ 2 root root 4096 Aug 28 21:10 src  
RUN ln -s /moasrc/moa-release*/ /moa \  
&& ln -s /moasrc/moa-release*/sizeofag*.jar /moa/sizeofag.jar  
  
# The two lines above enable the use of  
# /moa/moa.jar and /moa/sizeofag.jar  
# which resembles the manual more  
WORKDIR /moa  
  
#ENV MAXHEAP 512M # does not work, see:
https://github.com/moby/moby/issues/4783#issuecomment-221418846  
#ENTRYPOINT
["java","-Xmx\$MAXHEAP","-cp","moa.jar","-javaagent:sizeofag.jar","moa.DoTask"]  
ENTRYPOINT ["java","-cp","moa.jar","-javaagent:sizeofag.jar","moa.DoTask"]  
CMD
["LearnModel","-l","DecisionStump","-s","generators.WaveformGenerator","-m","1000000","-O","/tmp/model1.moa"]  

