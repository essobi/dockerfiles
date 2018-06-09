FROM fluent/fluentd:debian  
  
# 作成者情報  
MAINTAINER toshi <toshi@toshi.click>  
  
USER root  
  
# Debian set Locale  
RUN apt-get update && \  
apt-get -y install locales task-japanese && \  
locale-gen ja_JP.UTF-8 && \  
rm -rf /var/lib/apt/lists/*  
ENV LC_ALL=ja_JP.UTF-8 \  
LC_CTYPE=ja_JP.UTF-8 \  
LANGUAGE=ja_JP:jp  
RUN localedef -f UTF-8 -i ja_JP ja_JP.utf8  
  
# Debian set TimeZone  
ENV TZ=Asia/Tokyo  
RUN echo "${TZ}" > /etc/timezone && \  
rm /etc/localtime && \  
ln -s /usr/share/zoneinfo/Asia/Tokyo /etc/localtime && \  
dpkg-reconfigure -f noninteractive tzdata  
  
# コンテナのデバッグ等で便利なソフト導入しておく  
RUN apt-get update && \  
apt-get -y install vim && \  
apt-get -y install git && \  
apt-get -y install curl && \  
apt-get -y install wget && \  
apt-get -y install zip && \  
apt-get -y install unzip && \  
apt-get -y install ruby-dev && \  
apt-get -y install make && \  
apt-get -y install sudo && \  
apt-get -y install gcc && \  
apt-get -y install libc-dev && \  
rm -rf /var/lib/apt/lists/*  
  
# プラグイン導入  
RUN gem install fluent-plugin-rewrite-tag-filter && \  
gem install fluent-plugin-secure-forward --no-rdoc --no-ri && \  
gem install fluent-plugin-elasticsearch --no-rdoc --no-ri && \  
gem install fluent-plugin-record-reformer --no-rdoc --no-ri && \  
gem install fluent-plugin-cloudwatch-logs --no-rdoc --no-ri && \  
gem install fluent-plugin-ec2-metadata --no-rdoc --no-ri && \  
gem install fluent-plugin-s3 --no-rdoc --no-ri && \  
gem install fluent-plugin-slack --no-rdoc --no-ri && \  
gem install fluent-plugin-rewrite --no-rdoc --no-ri && \  
gem install fluent-plugin-tail-ex --no-rdoc --no-ri && \  
gem install fluent-plugin-forest --no-rdoc --no-ri && \  
gem install fluent-plugin-google-cloud --no-rdoc --no-ri  
  
# プラグインで必要となるソフトウェアの導入  
RUN apt-get update && \  
apt-get -y install net-tools && \  
apt-get -y install iproute2 && \  
apt-get -y install iputils-ping && \  
rm -rf /var/lib/apt/lists/*  
  
COPY fluent.conf /fluentd/etc/  
COPY entrypoint.sh /bin/  
RUN chmod +x /bin/entrypoint.sh  

