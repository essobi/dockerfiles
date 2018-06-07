FROM kalilinux/kali-linux-docker  
MAINTAINER Ralph May <ralph@thedarkcloud.net>  
  
RUN echo "deb http://http.kali.org/kali kali-rolling main contrib non-free" >
/etc/apt/sources.list && \  
echo "deb-src http://http.kali.org/kali kali-rolling main contrib non-free" >>
/etc/apt/sources.list  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -y update && apt-get -y dist-upgrade && apt-get clean  
RUN apt-get update && \  
apt-get install --no-install-recommends -y \  
python \  
ca-certificates \  
openssh-server \  
python-pip \  
libssl-dev \  
libffi-dev \  
python-dev \  
python-m2crypto \  
swig \  
lsb-release \  
git  
  
RUN pip install setuptools wheel  
RUN pip install pyopenssl  
RUN mkdir /root/empire  
RUN git clone https://github.com/PowerShellEmpire/Empire.git /root/empire  
ENV STAGING_KEY=RANDOM  
RUN bash -c "cd /root/empire/setup && /root/empire/setup/install.sh"  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /var/run/sshd  
RUN mkdir /root/.ssh  
COPY ./docker-entrypoint.sh /root/  
RUN chmod +x /root/docker-entrypoint.sh  
  
EXPOSE 22  
ENTRYPOINT ["/root/docker-entrypoint.sh"]

