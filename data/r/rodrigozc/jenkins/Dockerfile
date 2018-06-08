FROM jenkins/jenkins:lts  
MAINTAINER Rodrigo Zampieri Castilho <rodrigo.zampieri@gmail.com>  
  
USER root  
  
RUN apt-get update && apt-get install -y \--no-install-recommends apt-
transport-https ca-certificates curl software-properties-common python-
setuptools python-pip \  
&& wget -qO - https://download.docker.com/linux/debian/gpg | apt-key add \- \  
&& add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/debian $(lsb_release -cs) stable" \  
&& add-apt-repository "deb [arch=amd64] http://packages.cloud.google.com/apt
cloud-sdk-$(lsb_release -c -s) main" \  
&& apt-get update && apt-get -y \--allow-unauthenticated install docker-ce
google-cloud-sdk kubectl sudo locales bc \  
&& pip install awscli \  
&& awk '/exec java/{print " aws_configure.sh\n gcloud auth activate-service-
account --key-file=$GCLOUD_KEY_FILE\n nohup docker_auto_login.sh &"}1'
/usr/local/bin/jenkins.sh > /usr/local/bin/jenkins.sh.tmp \  
&& mv /usr/local/bin/jenkins.sh.tmp /usr/local/bin/jenkins.sh \  
&& chmod 775 /usr/local/bin/jenkins.sh \  
&& echo "pt_BR.UTF-8 UTF-8" > /etc/locale.gen \  
&& locale-gen pt_BR.UTF-8 \  
&& rm /etc/localtime \  
&& ln -s /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \  
&& usermod -a -G sudo jenkins \  
&& usermod -a -G staff jenkins \  
&& echo 'jenkins:welcome1' | chpasswd \  
&& curl -sL https://deb.nodesource.com/setup_6.x | bash - \  
&& apt-get install -y nodejs \  
&& npm install -g rimraf copyfiles \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /var/cache/* \  
&& touch /var/log/docker_auto_login.out \  
&& chown jenkins:jenkins /var/log/docker_auto_login.out  
  
ADD aws_configure.sh /usr/local/bin/  
ADD docker_login.sh /usr/local/bin/  
ADD docker_auto_login.sh /usr/local/bin/  
  
USER jenkins  
  
ENV AWS_DEFAULT_ACCESS_KEY_ID "changeit"  
ENV AWS_DEFAULT_SECRET_ACCESS_KEY "changeit"  
ENV AWS_DEFAULT_REGION "us-east-1"  
ENV AWS_DEFAULT_OUTPUT "json"  
  
ENV GCLOUD_KEY_FILE "changeit"  
  
ENV KUBECONFIG "changeit"  

