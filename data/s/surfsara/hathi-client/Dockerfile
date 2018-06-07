FROM openjdk:7-jre  
COPY . /hathi-client  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yq krb5-user \  
&& rm -rf /var/lib/apt/lists/* \  
&& /hathi-client/bin/get.sh hadoop spark \  
&& echo 'eval $(/hathi-client/bin/env.sh)' > /etc/profile.d/10-hathi.sh  
ENTRYPOINT [ "/bin/bash", "-l" ]  

