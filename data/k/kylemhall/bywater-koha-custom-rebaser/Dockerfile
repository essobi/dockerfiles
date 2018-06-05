FROM debian:stable-slim  
  
LABEL maintainer="kyle@bywatersolutions.com"  
  
ENV DO_IT 0  
RUN apt-get -y update \  
&& apt-get -y install \  
git-core \  
&& rm -rf /var/cache/apt/archives/* \  
&& rm -rf /var/lib/api/lists/*  
  
RUN git config --global user.email "kyle@bywatersolutions.com"  
RUN git config --global user.name "Kyle M Hall"  
  
WORKDIR /app  
ADD . /app  
  
CMD cd /kohaclone && perl /app/bws_rebase_branches.pl  

