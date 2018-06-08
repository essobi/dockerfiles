FROM jenkinsci/jnlp-slave:latest  
LABEL maintainer "Michael Kuroneko <hardwarehacking@gmail.com>"  
LABEL description="Flutter Develpment SDK"  
  
USER root  
ENV LANG en_US.UTF-8  
  
RUN echo 'deb http://us.archive.ubuntu.com/ubuntu precise main multiverse' >>
/etc/apt/sources.list \  
&& apt-key adv \--keyserver keyserver.ubuntu.com \--recv-keys 40976EAF437D05B5
\  
&& apt-get update -y \--force-yes \  
# Install dependencies  
&& apt-get install -y \--force-yes git wget unzip libgconf-2-4 gdb libstdc++6
libglu1-mesa fonts-droid-fallback lib32stdc++6 python3 \  
&& apt-get clean \  
# Install Flutter  
&& git clone https://github.com/flutter/flutter.git /usr/local/flutter \  
&& chown -R jenkins:jenkins /usr/local/flutter \  
# Install reviewdog  
&& curl -fSL
https://github.com/haya14busa/reviewdog/releases/download/0.9.8/reviewdog_linux_amd64
-o /usr/local/bin/reviewdog \  
&& chmod +x /usr/local/bin/reviewdog \  
&& chown jenkins:jenkins /usr/local/bin/reviewdog \  
# Install dartcop (dartanalyzer wrapper)  
&& curl -fSL
https://github.com/kuronekomichael/dartcop/raw/master/src/dartcop/dartcop.py
-o /usr/local/bin/dartcop \  
&& chmod +x /usr/local/bin/dartcop \  
&& chown jenkins:jenkins /usr/local/bin/dartcop  
# Setup Flutter  
USER jenkins  
ENV LANG en_US.UTF-8  
  
RUN /usr/local/flutter/bin/flutter doctor -v \  
&& rm -rfv /flutter/bin/cache/artifacts/gradle_wrapper  
# @see https://circleci.com/docs/2.0/high-uid-error/  
  
ENV PATH /usr/local/flutter/bin:/usr/local/flutter/bin/cache/dart-
sdk/bin:$PATH  
  

