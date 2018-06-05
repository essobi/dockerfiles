FROM ubuntu:trusty  
  
RUN echo "Asia/Yekaterinburg" > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure --frontend=noninteractive locales \  
&& update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV SPHINX_PACKAGE sphinxsearch_2.2.11-release-1~trusty_amd64.deb  
  
COPY sphinx-contrib-2.1.0.deb /tmp/sphinx-contrib-2.1.0.deb  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq \  
&& apt-get install -yq --no-install-recommends \  
curl \  
openssh-server \  
libpq5 \  
libmysqlclient18 \  
mysql-client \  
libodbc1 \  
unixodbc \  
&& curl -o /tmp/${SPHINX_PACKAGE}
http://sphinxsearch.com/files/${SPHINX_PACKAGE} \  
&& dpkg -i /tmp/${SPHINX_PACKAGE} \  
&& dpkg -i /tmp/sphinx-contrib-2.1.0.deb \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /tmp/sphinx-
contrib-2.1.0.deb\  
&& truncate -s 0 /var/log/*log  
  
RUN mkdir /var/run/sshd \  
&& sed -ri 's/UsePAM yes /#UsePAM yes/g' /etc/ssh/sshd_config \  
&& sed -ri 's/#UsePAM no/UsePAM no/g' /etc/ssh/sshd_config \  
&& sed -ri 's/#PasswordAuthentication/PasswordAuthentication/g'
/etc/ssh/sshd_config \  
&& sed -ri 's/PasswordAuthentication no/PasswordAuthentication yes/g'
/etc/ssh/sshd_config  
  
RUN useradd -ms /bin/bash sphinx \  
&& echo "sphinx:secret" | chpasswd  
  
ENV SPHINXDATA /sphinx  
VOLUME /sphinx  
  
COPY entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
EXPOSE 22 9306 9312  
CMD ["sshd"]  

