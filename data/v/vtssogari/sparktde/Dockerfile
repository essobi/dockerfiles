FROM centos:7  
WORKDIR /app  
  
ENV TABLEAU_SDK_VERSION 9-2-0  
RUN yum install -y java-sdk unzip ant vim wget \  
&& mkdir -p /sdk \  
&& wget -O /sdk/tableau_sdk.zip
https://downloads.tableau.com/tssoftware/Tableau-SDK-C-
Java-64Bit-$TABLEAU_SDK_VERSION.zip \  
&& wget -O /sdk/tableau_sdk.rpm
https://downloads.tableau.com/tssoftware/Tableau-SDK-
Linux-64Bit-$TABLEAU_SDK_VERSION.rpm \  
&& cd /sdk \  
&& unzip tableau_sdk.zip \  
&& rm /sdk/tableau_sdk.zip \  
&& rpm -ivh tableau_sdk.rpm \  
&& mkdir -p /spark \  
&& cd /spark \  
&& wget -O spark-2.2.0-bin-hadoop2.6.tgz
https://d3kbcqa49mib13.cloudfront.net/spark-2.2.0-bin-hadoop2.6.tgz \  
&& tar -xvzf spark-2.2.0-bin-hadoop2.6.tgz \  
&& cd /tmp \  
&& curl --silent --location https://rpm.nodesource.com/setup_6.x | bash - \  
&& yum -y install nodejs \  
&& mkdir -p /app \  
&& mkdir -p /data \  
&& mkdir -p /output  
  
COPY build.xml /sdk  
COPY SparkTDE-assembly-1.0.jar /app  
RUN mkdir -p /spark/hadoop/conf  
COPY extract.scala /app  
COPY publish.scala /app  
COPY spark-env.sh /spark/spark-2.2.0-bin-hadoop2.6/conf  
COPY ./docker-entrypoint.sh /  
COPY ts-api_2_1.xsd /app  
COPY ts-api_2_2.xsd /app  
COPY ts-api_2_3.xsd /app  
COPY ts-api_2_4.xsd /app  
COPY ts-api_2_5.xsd /app  
COPY ts-api_2_6.xsd /app  
ENTRYPOINT ["/docker-entrypoint.sh"]

