# Используем за основу контейнера Ubuntu 16.04 LTS  
FROM ubuntu:16.04  
# Переключаем Ubuntu в неинтерактивный режим — чтобы избежать лишних запросов  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get install -y python-software-properties  
RUN apt-get install -y debconf-utils  
RUN apt-get install -y software-properties-common  
RUN apt-get install locales  
RUN locale-gen ru_RU  
RUN locale-gen ru_RU.UTF-8  
RUN update-locale  
RUN dpkg-reconfigure locales  
  
#ставим джаву  
RUN add-apt-repository -y ppa:webupd8team/java  
RUN apt-get update  
RUN echo "oracle-java8-installer shared/accepted-oracle-license-v1-1 select
true" | debconf-set-selections  
RUN apt-get install -y oracle-java8-installer  
  
RUN java -version  
  
#ставим sbt  
RUN apt-get install -y apt-transport-https  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv
2EE0EA64E40A89B84B2DF73499E82A75642AC823  
RUN apt-get update  
RUN apt-get install -y sbt  
  
#ставим ноду  
RUN apt-get install -y curl  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -y nodejs  
RUN apt-get update --fix-missing  
RUN apt-get install -y build-essential  
RUN apt-get install -y make  
RUN npm install -g gulp  
  
CMD ["sh", "-c", "${RUN_SCRIPT}"]  

