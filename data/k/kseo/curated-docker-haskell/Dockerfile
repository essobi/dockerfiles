FROM haskell:8.0  
MAINTAINER Kwang Yul Seo <kwangyul.seo@gmail.com>  
  
ADD packages.txt /  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends libicu-dev && \  
rm -rf /var/lib/apt/lists/*  
  
RUN useradd -ms /bin/bash haskellpad  
USER haskellpad  
  
WORKDIR /home/haskellpad  
RUN stack install $(cat /packages.txt)  
  
CMD ["ghci"]  

