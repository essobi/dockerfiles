FROM selenium/standalone-chrome  
  
#=================  
# Locale settings  
#=================  
USER root  
ENV LANGUAGE ru_RU.UTF-8  
ENV LANG ru_RU.UTF-8  
RUN locale-gen ru_RU.UTF-8 \  
&& dpkg-reconfigure --frontend noninteractive locales \  
&& apt-get update -qqy \  
&& apt-get -qqy --no-install-recommends install \  
language-pack-en \  
language-pack-ru \  
&& rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
USER seluser

