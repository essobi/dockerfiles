FROM ubuntu:xenial  
MAINTAINER rapid.recon@birchwood.ca  
ENV OS_LOCALE="en_US.UTF-8"  
RUN apt-get update && apt-get install -y locales git curl bash && locale-gen
${OS_LOCALE}  
ENV LANG=${OS_LOCALE} \  
LANGUAGE=en_US:en \  
LC_ALL=${OS_LOCALE}  
  
RUN curl -sL https://deb.nodesource.com/setup_7.x | bash - \  
&& apt-get install -y nodejs  
  
# Install FPM  
RUN npm -g install gulp \  
&& npm -g install webpack \  
&& gulp -v \  
&& webpack -v

