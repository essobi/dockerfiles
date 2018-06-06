FROM yuwash/pandoc-citeproc-european  
LABEL maintainer "Yushin Washio <yuwash at yandex dot com>"  
  
RUN set -ex \  
&& apt-get update && apt-get install -y --no-install-recommends \  
texlive-fonts-extra \  
&& rm -rf /var/lib/apt/lists/*  

