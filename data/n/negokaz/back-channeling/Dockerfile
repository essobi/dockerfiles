FROM java:openjdk-8  
MAINTAINER negokaz <negokaz@gmail.com>  
  
ENV BACK_CHANNELING_VERSION 0.2.0-beta1  
ENV DATOMIC_URL datomic:free://localhost:4334/bc  
  
RUN curl --silent --location \  
\--url "https://github.com/kawasima/back-
channeling/releases/download/v${BACK_CHANNELING_VERSION}/back-
channeling-${BACK_CHANNELING_VERSION}-dist.zip" \  
\--output back-channeling.zip \  
&& unzip back-channeling.zip \  
&& rm back-channeling.zip \  
&& mv "back-channeling-${BACK_CHANNELING_VERSION}" "/opt/back-channeling"  
  
WORKDIR /opt/back-channeling  
  
ADD entrypoint.sh bin/  
RUN chmod a+x bin/entrypoint.sh  
  
VOLUME ["/opt/datomic/data"]  
  
EXPOSE 3009  
ENTRYPOINT ["bin/entrypoint.sh"]  

