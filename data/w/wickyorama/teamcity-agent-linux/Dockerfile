FROM jetbrains/teamcity-agent:latest  
  
MAINTAINER Wickstargazer <wickyorama@gmail.com>  
  
COPY configure.sh /configure.sh  
  
ENV AWS_REGION "ap-southeast-1"  
RUN apt-get update  
RUN apt-get -qy install python-pip  
RUN pip install awscli  
RUN curl -LO https://storage.googleapis.com/kubernetes-
release/release/v1.8.0/bin/linux/amd64/kubectl  
RUN chmod +x ./kubectl  
RUN mv ./kubectl /usr/local/bin/kubectl  
  
VOLUME "/opt/buildagent/work"  
  
RUN chmod +x /configure.sh && sync  
  
CMD [ "/configure.sh"]

