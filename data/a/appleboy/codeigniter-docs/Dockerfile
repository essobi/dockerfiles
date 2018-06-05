FROM python:2.7.13  
RUN apt-get -qq update && apt-get -qqy install locales && rm -rf
/var/lib/apt/lists/*  
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen  
RUN sed -i -e 's/# zh_TW.UTF-8 UTF-8/zh_TW.UTF-8 UTF-8/' /etc/locale.gen  
RUN sed -i -e 's/# zh_TW BIG5/zh_TW BIG5/' /etc/locale.gen  
RUN dpkg-reconfigure --frontend=noninteractive locales  
RUN update-locale LANG=en_US.UTF-8 && \  
echo "LANGUAGE=en_US.UTF-8" >> /etc/default/locale && \  
echo "LC_ALL=en_US.UTF-8" >> /etc/default/locale  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
RUN pip install "sphinx==1.2.3"  
RUN pip install "sphinxcontrib-phpdomain==0.1.3.post1"  

