FROM ruby:2.1  
MAINTAINER harmon25 "nomraharmon@gmail.com"  
ENV NMAP_VERSION 7.01  
RUN apt-get update && apt-get -y install \  
\--no-install-recommends \  
bison \  
libbison-dev \  
libpcap-dev \  
libpcap0.8 \  
libpcap0.8-dev \  
postgresql-client \  
build-essential \  
wget \  
bzip2 \  
tmux \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN wget https://nmap.org/dist/nmap-${NMAP_VERSION}.tar.bz2 \  
&& bzip2 -cd nmap-${NMAP_VERSION}.tar.bz2 | tar xvf - \  
&& cd nmap-${NMAP_VERSION} \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -rf /nmap-${NMAP_VERSION} \  
&& rm -rf /nmap-${NMAP_VERSION}.tar.bz2  
  
RUN git clone \--depth=1 https://github.com/rapid7/metasploit-framework.git \  
&& cd metasploit-framework \  
&& bundle install  
  
COPY cleanup.sh /  
  
RUN bash /cleanup.sh  
  
ENV PATH=$PATH:/metasploit-framework  
  
ENV MSF_DATABASE_CONFIG /metasploit-framework/config/database.yml  
ENV PGPASSFILE /.pgpass  
  
COPY pentest.rb /metasploit-framework/plugins/  
COPY entrypoint.sh /  
  
WORKDIR /metasploit-framework  
  
EXPOSE 55553  
ENTRYPOINT ["/entrypoint.sh"]

