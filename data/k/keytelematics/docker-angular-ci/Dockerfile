FROM shusson/chrome-tester  
  
RUN apt-get update && apt-get install python python-pip jq gettext -y && \  
pip install awscli && \  
apt-get remove python-pip -y && \  
apt-get autoclean -y && apt-get clean -y  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT [ "/entrypoint.sh" ]

