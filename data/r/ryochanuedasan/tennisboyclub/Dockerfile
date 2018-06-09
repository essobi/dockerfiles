FROM centos:7  
# DNSサーバーをgoogleのものにする  
# RUN cat /etc/resolv.conf  
# RUN sed -e "/8.8.8.8/d" /etc/resolv.conf > /etc/resolv.conf  
# RUN echo "nameserver 8.8.8.8" >> /etc/resolv.conf  
# 必要なコマンドインストール  
RUN yum install -y wget  
RUN yum install -y unzip  
RUN yum install -y git  
  
# Javaインストール  
RUN yum install -y java  
  
# Xvfbインストール  
RUN yum install -y xorg-x11-server-Xvfb  
  
# sbtインストール  
RUN curl https://bintray.com/sbt/rpm/rpm | tee /etc/yum.repos.d/bintray-sbt-
rpm.repo  
RUN yum -y install sbt  
  
# Scalaインストール  
RUN cd /usr/local/lib/ && \  
wget http://downloads.typesafe.com/scala/2.11.7/scala-2.11.7.tgz && \  
tar zxvf scala-2.11.7.tgz && \  
ln -s scala-2.11.7 scala  
RUN echo 'export SCALA_HOME=/usr/local/lib/scala' >> /etc/profile.d/scala.sh  
RUN echo 'export PATH=$PATH:$SCALA_HOME/bin' >> /etc/profile.d/scala.sh  
RUN source /etc/profile.d/scala.sh  
  
# chromeインストール  
RUN cd /usr/local/lib && \  
wget https://chrome.richardlloyd.org.uk/install_chrome.sh && \  
chmod u+x install_chrome.sh && \  
./install_chrome.sh -f && \  
  
# chromedriverインストール  
wget http://chromedriver.storage.googleapis.com/2.27/chromedriver_linux64.zip
&& \  
unzip chromedriver_linux64.zip && \  
cp chromedriver /opt/google/chrome/ && \  
cd /opt/google/chrome/ && \  
cp google-chrome google-chromedriver && \  
  
# chromedriverの設定ファイルを編集  
sed -i -e "55d" google-chromedriver && \  
sed -i -e "55i\ exec -a \"\$\0\" \"\$HERE\/chromedriver\" \"\$\@\"" google-
chromedriver  
  
# chromedriverつづき  
RUN ln -s /opt/google/chrome/google-chromedriver /usr/bin/chromedriver  
RUN chmod 777 /opt/google/chrome/chromedriver  
  
# seleniumインストール  
RUN cd /usr/local/lib/ && \  
wget http://selenium-release.storage.googleapis.com/3.0/selenium-server-
standalone-3.0.1.jar  

