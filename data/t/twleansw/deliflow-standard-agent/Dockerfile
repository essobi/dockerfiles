FROM gocd/gocd-agent:16.2.1  
MAINTAINER YunLong <yunl.zheng@gmail.com>  
  
WORKDIR /tmp  
  
RUN apt-get update && apt-get install openjdk-7-jdk -y && apt-get clean && rm
-rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
RUN curl -O
https://archive.apache.org/dist/maven/maven-3/3.0.5/binaries/apache-
maven-3.0.5-bin.zip && unzip apache-maven-3.0.5-bin.zip && mv apache-
maven-3.0.5 /usr/local/maven && rm -rf apache-maven-3.0.4-bin.zip  
RUN curl -O http://repo1.maven.org/maven2/org/codehaus/sonar/runner/sonar-
runner-dist/2.4/sonar-runner-dist-2.4.zip && unzip sonar-runner-dist-2.4.zip
&& mv sonar-runner-2.4 /usr/local/sonar-runner && rm -rf sonar-runner-
dist-2.4.zip  
ENV PATH /usr/local/maven/bin:/usr/local/sonar-runner/bin:$PATH  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
CMD ["/sbin/my_init"]  

