FROM ubuntu:17.10  
MAINTAINER Piotr Krzemiński (pio.krzeminski@gmail.com)  
  
RUN apt-get update && apt-get install -y dirmngr ca-certificates wget  
  
RUN echo "deb https://dl.bintray.com/sbt/debian /" | tee -a
/etc/apt/sources.list.d/sbt.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
2EE0EA64E40A89B84B2DF73499E82A75642AC823 \  
&& echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu artful main" |
tee /etc/apt/sources.list.d/webupd8team-java.list \  
&& apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 \--recv-keys EEA14886
\  
&& echo "deb http://apt.postgresql.org/pub/repos/apt/ zesty-pgdg main" | tee
/etc/apt/sources.list.d/pgdg.list \  
&& wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-
key add \- \  
&& apt-get update  
  
RUN apt-get install -y postgresql-10 \  
&& echo "local all postgres trust" > /etc/postgresql/10/main/pg_hba.conf \  
&& echo "host all postgres 127.0.0.1/32 trust" >>
/etc/postgresql/10/main/pg_hba.conf  
  
RUN echo yes | apt-get install -y oracle-java8-installer \  
&& update-java-alternatives -s java-8-oracle  
  
RUN apt-get install -y sbt scala nodejs npm  
  
RUN npm install -g elm elm-test elm-github-install elm-format newman  
  
RUN apt-get install -y build-essential chrpath libssl-dev libxft-dev
libfreetype6 libfreetype6-dev libfontconfig1 libfontconfig1-dev \  
&& export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64" \  
&& cd /tmp \  
&& wget
https://github.com/Medium/phantomjs/releases/download/v2.1.1/$PHANTOM_JS.tar.bz2
\  
&& tar xvjf $PHANTOM_JS.tar.bz2 \  
&& mv $PHANTOM_JS /usr/local/share \  
&& ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin \  
&& cd $OLDPWD \  
&& rm -fr /tmp/phantom*  
  
RUN wget https://repo1.maven.org/maven2/org/flywaydb/flyway-
commandline/5.0.7/flyway-commandline-5.0.7-linux-x64.tar.gz -O
/tmp/flyway.tar.gz \  
&& tar -zxvf /tmp/flyway.tar.gz -C /usr/local/share \  
&& ln -s /usr/local/share/flyway-5.0.7/flyway /usr/local/bin/flyway \  
&& rm -f /tmp/flyway.tar.gz  

