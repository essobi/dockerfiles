FROM centos:centos7  
  
ADD CentOS7-Base-163.repo /etc/yum.repos.d/CentOS-Base.repo  
RUN yum -y update; yum clean all  
RUN yum install -y epel-release  
RUN yum -y install epel-release python-pip mesa-dri-drivers libexif
libcanberra-gtk2 libcanberra xorg-x11-server-Xvfb python-dev python-crypto
python-devel mysql-devel gcc unzip wget; yum clean all  
  
ADD http://dev.mysql.com/get/mysql-community-release-el7-5.noarch.rpm /mysql-
community-release-el7-5.noarch.rpm  
RUN yum -y install /mysql-community-release-el7-5.noarch.rpm  
RUN yum clean all  
RUN rm /mysql-community-release-el7-5.noarch.rpm  
  
RUN pip install --upgrade pip  
ADD requirements.txt /requirements.txt  
RUN pip install -r /requirements.txt  
  
ADD run.sh /usr/local/bin/run.sh  
RUN chmod +x /usr/local/bin/run.sh  
  
RUN wget https://archive.org/download/Google-Chrome-Legacy-Versions/google-
chrome-stable-50.0.2661.86-1.x86_64.rpm \  
&& yum -y install /google-chrome*.rpm \  
&& rm /google-chrome*.rpm  
  
RUN wget
https://chromedriver.storage.googleapis.com/2.22/chromedriver_linux64.zip \  
&& unzip chromedriver_linux64.zip \  
&& rm chromedriver_linux64.zip \  
&& chmod +x chromedriver \  
&& mv -f chromedriver /usr/local/share/chromedriver \  
&& ln -sf /usr/local/share/chromedriver /usr/local/bin/chromedriver \  
&& ln -sf /usr/local/share/chromedriver /usr/bin/chromedriver  
  
CMD ["run.sh"]  

