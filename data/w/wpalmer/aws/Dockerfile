FROM python  
RUN pip install \--upgrade pip \  
&& pip install awscli \  
&& apt-get update \  
&& apt-get install -y groff jq less \  
&& apt-get install \--no-install-recommends -y cron \  
&& rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/sbin/cron", "-f"]  

