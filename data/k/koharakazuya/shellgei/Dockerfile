FROM buildpack-deps:jessie-curl  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
git \  
less \  
locales \  
man-db \  
manpages \  
manpages-ja \  
nkf \  
openssh-client \  
vim \  
&& locale-gen ja_JP.UTF-8 \  
&& localedef -f UTF-8 -i ja_JP ja_JP \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:jp  
ENV LC_ALL ja_JP.UTF-8  
  
CMD ["/bin/bash"]  

