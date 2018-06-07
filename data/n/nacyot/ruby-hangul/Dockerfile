FROM dockerfile/ruby  
  
RUN apt-get update  
RUN apt-get install -y language-pack-en language-pack-ko  
RUN locale-gen ko_KR.UTF-8  
ENV LANGUAGE ko_KR.UTF-8  
ENV LANG ko_KR.UTF-8  
ENV LC_ALL ko_KR.UTF-8  
ENV LC_CTYPE ko_KR.UTF-8  
ENV LC_NUMERIC ko_KR.UTF-8  
ENV LC_TIME ko_KR.UTF-8  
ENV LC_COLLATE ko_KR.UTF-8  
ENV LC_MONETARY ko_KR.UTF-8  
ENV LC_MESSAGES ko_KR.UTF-8  
ENV LC_PAPER ko_KR.UTF-8  
ENV LC_NAME ko_KR.UTF-8  
ENV LC_ADDRESS ko_KR.UTF-8  
ENV LC_TELEPHONE ko_KR.UTF-8  
ENV LC_MEASUREMENT ko_KR.UTF-8  
ENV LC_IDENTIFICATION ko_KR.UTF-8  
RUN dpkg-reconfigure locales  

