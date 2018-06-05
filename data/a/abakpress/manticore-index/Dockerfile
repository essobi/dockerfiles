FROM ubuntu:trusty  
  
RUN echo "Asia/Yekaterinburg" > /etc/timezone \  
&& dpkg-reconfigure -f noninteractive tzdata \  
&& locale-gen en_US.UTF-8 \  
&& dpkg-reconfigure --frontend=noninteractive locales \  
&& update-locale LANG=en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
ENV MANTICORE_VERSION 2.6.2  
ENV MANTICORE_PACKAGE manticore_${MANTICORE_VERSION}-180223-0bbd194-release-
stemmer.trusty_amd64-bin.deb  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -qq \  
&& apt-get install -yq --no-install-recommends \  
git \  
wget \  
openssh-server \  
libpq5 \  
libmysqlclient18 \  
mysql-client \  
libodbc1 \  
unixodbc \  
ca-certificates \  
&& update-ca-certificates \  
&& cd /tmp && wget
https://github.com/manticoresoftware/manticoresearch/releases/download/${MANTICORE_VERSION}/${MANTICORE_PACKAGE}
\  
&& dpkg -i /tmp/${MANTICORE_PACKAGE} \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
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
  
ENV MANTICOREDATA /sphinx  
VOLUME /sphinx  
  
COPY entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
EXPOSE 22 9306 9312  
CMD ["sshd"]  

