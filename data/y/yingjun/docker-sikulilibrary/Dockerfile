FROM ubuntu:16.04  
MAINTAINER Ying <wandy1208@gmail.com>  
  
ENV ROOT_PASSWORD root  
  
RUN apt-get -qqy update \  
&& apt-get -qqy --no-install-recommends install \  
python2.7 \  
python-pip \  
python-lxml \  
bash \  
wget \  
curl \  
unzip \  
git  
  
RUN pip install --upgrade setuptools  
RUN pip install -U robotframework==3.0.2 \  
robotframework-SikuliLibrary  
  
  
#ssh-server  
RUN apt-get -qqy update \  
&& apt-get -qqy install -y openssh-server \  
&& mkdir /var/run/sshd \  
&& echo "root:${ROOT_PASSWORD}" | chpasswd \  
&& sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
\  
&& sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
COPY entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/entrypoint.sh  
  
# RUN chmod +x /usr/lib/python2.7/site-
packages/SikuliLibrary/lib/SikuliLibrary.jar  
# RUN java -jar /usr/lib/python2.7/site-
packages/SikuliLibrary/lib/SikuliLibrary.jar 18181 &  
RUN chmod +x /usr/local/lib/python2.7/dist-
packages/SikuliLibrary/bin/SikuliLibrary.jar  
RUN java -jar /usr/local/lib/python2.7/dist-
packages/SikuliLibrary/bin/SikuliLibrary.jar 18181 &  
  
EXPOSE 22  
EXPOSE 18181  
ENTRYPOINT ["entrypoint.sh"]

