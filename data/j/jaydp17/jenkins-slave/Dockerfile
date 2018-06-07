FROM evarga/jenkins-slave  
  
LABEL maintainer Jaydeep Solanki <jaydp17@gmail.com> (https://jaydp.com)  
  
RUN apt-get update && apt-get install -y \--no-install-recommends curl git \  
&& apt-get -q autoremove \  
&& apt-get -q clean -y && rm -rf /var/lib/apt/lists/* && rm -f
/var/cache/apt/*.bin \  
&& /var/lib/dpkg/info/ca-certificates-java.postinst configure  

