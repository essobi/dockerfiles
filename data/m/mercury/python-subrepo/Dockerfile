FROM python:3.6-stretch  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
less \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone --depth=1 \--branch=0.3.1 https://github.com/ingydotnet/git-
subrepo.git /tmp/git-subrepo \  
&& cd /tmp/git-subrepo \  
&& make install \  
&& cd - \  
&& rm -rf /tmp/git-subrepo  

