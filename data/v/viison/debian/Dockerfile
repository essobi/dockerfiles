FROM debian:squeeze  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV TZ=Europe/Berlin  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN echo "deb http://archive.debian.org/debian/ squeeze main" >
/etc/apt/sources.list \  
&& echo "deb http://archive.debian.org/debian/ squeeze-lts main" >>
/etc/apt/sources.list \  
&& apt-get -o Acquire::Check-Valid-Until=false update \  
&& apt-get install --no-install-recommends -y \  
locales \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN echo "de_DE.UTF-8 UTF-8" > /etc/locale.gen && locale-gen  
ENV LANG de_DE.UTF-8  

