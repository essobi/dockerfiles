FROM alpine  
  
USER root  
WORKDIR /root  
  
RUN apk add --no-cache \  
curl \  
man \  
py-pip \  
task \  
task-doc  
  
RUN pip install \  
bugwarrior \  
bugwarrior[jira] \  
taskwarrior-blocks-capsule  
  
RUN curl -SOs
https://gist.githubusercontent.com/BrianHicks/2769821/raw/7b6adf5b074d9959aafb248cc9c0fd58e047e704/graphdeps.py
\  
&& chmod +x graphdeps.py  
  
COPY defaults.rc defaults.rc  
COPY taskbw .config/bugwarrior/bugwarriorrc  
  
RUN dos2unix defaults.rc .config/bugwarrior/bugwarriorrc \  
&& chmod -x defaults.rc .config/bugwarrior/bugwarriorrc \  
&& mkdir .task  
  
VOLUME /root/.task/  
WORKDIR /root/work  
ENTRYPOINT [ "task" ]  
  

