# stretch  
FROM debian:stable-20170620  
LABEL maintainer="mihailldn<mihail.ivanov@cloudreach.com>"  
  
ENV sceptre 1.2.0  
ENV workdir /sceptre_project  
  
VOLUME $workdir  
WORKDIR $workdir  
  
USER root  
  
ADD requirements.txt /tmp/requirements.txt  
  
RUN apt-get update && apt-get install -y \  
python \  
python-pip \  
&& pip install -r /tmp/requirements.txt \  
&& pip install sceptre==${sceptre}  
  
CMD ["bash"]

