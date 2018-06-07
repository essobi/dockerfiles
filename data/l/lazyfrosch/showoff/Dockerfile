FROM ruby:2.3  
RUN apt-get update \  
&& apt-get install -y git locales \  
&& rm -rf /var/lib/apt/lists/* \  
&& curl -LsS "https://github.com/tianon/gosu/releases/download/1.10/gosu-
amd64" > /usr/sbin/gosu \  
&& chmod +x /usr/sbin/gosu  
  
ENV LANG=en_US.UTF-8 \  
LANGUAGE=en_US:en \  
LC_ALL=en_US.UTF-8 \  
SHOWOFF_VERSION=0.9.11.1  
RUN echo "${LANG}" "$(echo "${LANG}" | sed 's/.*\\.\\(\S\\+\\)$/\1/')"
>/etc/locale.gen \  
&& locale-gen \  
&& gem install showoff --version=${SHOWOFF_VERSION}  
  
VOLUME /showoff  
  
EXPOSE 9090  
COPY entrypoint.sh /entrypoint  
ENTRYPOINT [ "/entrypoint" ]  
CMD showoff serve  

