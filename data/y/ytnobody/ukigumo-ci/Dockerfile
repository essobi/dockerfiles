FROM ytnobody/base:wheezy  
MAINTAINER ytnobody <ytnobody@gmail.com>  
  
RUN mv /bin/sh /bin/ash && ln -s /bin/bash /bin/sh  
RUN curl -L http://is.gd/plenvsetup | /bin/sh  
  
RUN source /root/.bash_profile && \  
plenv install 5.10.1 --as 5.10 && \  
plenv global 5.10 && \  
plenv install-cpanm && \  
plenv rehash  
  
RUN source /root/.bash_profile && \  
plenv install 5.12.5 --as 5.12 && \  
plenv global 5.12 && \  
plenv install-cpanm && \  
plenv rehash  
  
RUN source /root/.bash_profile && \  
plenv install 5.14.4 --as 5.14 && \  
plenv global 5.14 && \  
plenv install-cpanm && \  
plenv rehash  
  
RUN source /root/.bash_profile && \  
plenv install 5.16.3 --as 5.16 && \  
plenv global 5.16 && \  
plenv install-cpanm && \  
plenv rehash  
  
RUN source /root/.bash_profile && \  
plenv install 5.18.4 --as 5.18 && \  
plenv global 5.18 && \  
plenv install-cpanm && \  
plenv rehash  
  
RUN source /root/.bash_profile && \  
plenv install 5.20.3 --as 5.20 && \  
plenv global 5.20 && \  
plenv install-cpanm && \  
plenv rehash  
  
RUN mkdir -pv /usr/local/ukigumo  
  
COPY ukigumo/config.pl /usr/local/ukigumo/  
  
COPY ukigumo/Procfile /usr/local/ukigumo/  
  
COPY ukigumo/cpanfile /usr/local/ukigumo/  
  
WORKDIR /usr/local/ukigumo  
  
RUN source /root/.bash_profile && \  
cpanm -n --installdeps .  
  
RUN mkdir -pv /opt/ukigumo  
  
VOLUME /opt/ukigumo  
  
EXPOSE 2828  
EXPOSE 2829  
ENTRYPOINT source /root/.bash_profile && \  
proclet start  
  

