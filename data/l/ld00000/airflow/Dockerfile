FROM ubuntu:14.04  
MAINTAINER ld00000 <lidong9144@163.com>  
  
ARG AIRFLOW_VERSION=1.7.1.3  
ENV AIRFLOW_HOME /airflow  
  
RUN apt-get autoclean && apt-get --purge -y autoremove  
RUN mv /etc/apt/sources.list /etc/apt/sources.list.bak  
ADD conf/163-sources.list /etc/apt/sources.list  
  
# timezone  
ENV TZ=Asia/Shanghai  
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone  
  
RUN apt-get update  
RUN echo y | apt-get install wget  
RUN wget https://bootstrap.pypa.io/get-pip.py --no-check-certificate  
  
# airflow dep  
RUN echo y | apt-get install \  
libxml2-dev \  
libxslt1-dev \  
zlib1g-dev \  
libevent-dev \  
libmysqlclient-dev \  
libkrb5-dev \  
libsasl2-dev \  
libssl-dev \  
libffi-dev \  
libpq-dev \  
build-essential \  
libblas-dev \  
liblapack-dev \  
curl  
  
# RUN echo y | apt-get autoremove python3.4  
RUN echo y | apt-get install python2.7  
# RUN update-alternatives --install /usr/bin/python python /usr/bin/python2.7
100  
RUN echo y | apt-get install python3-dev python-pip python-dev  
  
# install airflow  
# RUN easy_install -U setuptools  
RUN pip install -i http://pypi.douban.com/simple/ Cython \  
&& pip install -i http://pypi.douban.com/simple/ flask-bcrypt \  
&& pip install -i http://pypi.douban.com/simple/ pytz==2015.7 \  
&& pip install -i http://pypi.douban.com/simple/ cryptography \  
&& pip install -i http://pypi.douban.com/simple/ pyOpenSSL \  
&& pip install -i http://pypi.douban.com/simple/ ndg-httpsclient \  
&& pip install -i http://pypi.douban.com/simple/ pyasn1 \  
&& pip install -i http://pypi.douban.com/simple/ psycopg2 \  
&& pip install -i http://pypi.douban.com/simple/ pandas==0.18.1 \  
&& pip install -i http://pypi.douban.com/simple/ celery==3.1.23 \  
&& pip install -i http://pypi.douban.com/simple/
airflow[mysql,celery,hive,hdfs,jdbc]==$AIRFLOW_VERSION  
  
# jdk  
ENV VERSION 8  
ENV UPDATE 111  
ENV BUILD 14  
ENV JAVA_HOME /usr/lib/jvm/java-${VERSION}-oracle  
ENV JRE_HOME ${JAVA_HOME}/jre  
  
RUN wget --no-check-certificate --no-cookies --header "Cookie:
oraclelicense=accept-securebackup-cookie" \  
-P /tmp \  
http://download.oracle.com/otn-
pub/java/jdk/"${VERSION}"u"${UPDATE}"-b"${BUILD}"/jdk-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz  
  
RUN cd /tmp && tar -zxvf jdk-"${VERSION}"u"${UPDATE}"-linux-x64.tar.gz && \  
mkdir -p /usr/lib/jvm && mv /tmp/jdk1.${VERSION}.0_${UPDATE} "${JAVA_HOME}" &&
\  
rm -rf /tmp/*  
  
RUN update-alternatives --install "/usr/bin/java" "java"
"${JRE_HOME}/bin/java" 1 && \  
update-alternatives --install "/usr/bin/javac" "javac"
"${JAVA_HOME}/bin/javac" 1 && \  
update-alternatives --set java "${JRE_HOME}/bin/java" && \  
update-alternatives --set javac "${JAVA_HOME}/bin/javac"  
  
RUN apt-get clean \  
&& rm -fr /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/usr/share/man \  
/usr/share/doc \  
/usr/share/doc-base  
  
COPY script/entrypoint.sh ${AIRFLOW_HOME}/entrypoint.sh  
COPY conf/airflow.cfg ${AIRFLOW_HOME}/airflow.cfg  
COPY script/authentication.py ${AIRFLOW_HOME}/authentication.py  
  
EXPOSE 8080 5555 8793  
RUN groupadd -r airflow && useradd -r -g airflow airflow  
RUN (echo "airflow";sleep 1;echo "airflow") | passwd airflow > /dev/null  
  
RUN chown -R airflow: ${AIRFLOW_HOME} \  
&& chmod +x ${AIRFLOW_HOME}/entrypoint.sh \  
&& chmod +x ${AIRFLOW_HOME}/authentication.py  
  
USER airflow  
WORKDIR ${AIRFLOW_HOME}  
  
ENTRYPOINT ["./entrypoint.sh"]  

