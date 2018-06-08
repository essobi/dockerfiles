FROM debian:stretch  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN echo 'APT::Install-Suggests "false";' >> /etc/apt/apt.conf  
  
RUN apt-get -qq update \  
&& apt-get -qq check \  
&& apt-get -qq install -y apt-utils \  
&& apt-get -qq install -f \  
&& apt-get -qq upgrade -y \  
&& apt-get -qq install -y apt-transport-https locales curl unzip bzip2 vim \  
&& apt-get -qq clean  
  
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \  
&& locale-gen en_US.UTF-8 \  
&& update-locale LANG=en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  

