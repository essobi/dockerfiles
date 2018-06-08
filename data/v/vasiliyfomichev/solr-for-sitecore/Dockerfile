FROM java:8  
MAINTAINER Vasiliy Fomichev "vasya.fomichev@gmail.com"  
ENV SOLR_VERSION 5.2.1  
ENV SOLR solr-$SOLR_VERSION  
ENV SOLR_USER solr  
ENV SOLR_PATH /opt/$SOLR/server/solr  
  
RUN export DEBIAN_FRONTEND=noninteractive && \  
apt-get update && \  
apt-get -y install \  
curl \  
lsof \  
procps && \  
groupadd -r $SOLR_USER && \  
useradd -r -g $SOLR_USER $SOLR_USER && \  
mkdir -p /opt && \  
wget -nv --output-document=/opt/$SOLR.tgz
http://www.us.apache.org/dist/lucene/solr/$SOLR_VERSION/$SOLR.tgz && \  
tar -C /opt --extract --file /opt/$SOLR.tgz && \  
rm /opt/$SOLR.tgz && \  
ln -s /opt/$SOLR /opt/solr && \  
chown -R $SOLR_USER:$SOLR_USER /opt/solr /opt/$SOLR  
  
# Adding sitecore_master_index core  
RUN cp -af $SOLR_PATH/configsets/basic_configs
$SOLR_PATH/sitecore_master_index  
COPY schema.xml $SOLR_PATH/sitecore_master_index/conf/  
RUN echo name=sitecore_master_index >
$SOLR_PATH/sitecore_master_index/core.properties  
  
# Adding sitecore_web_index core  
RUN cp -af $SOLR_PATH/configsets/basic_configs $SOLR_PATH/sitecore_web_index  
COPY schema.xml $SOLR_PATH/sitecore_web_index/conf/  
RUN echo name=sitecore_web_index >
$SOLR_PATH/sitecore_web_index/core.properties  
  
# Adding sitecore_core_index core  
RUN cp -af $SOLR_PATH/configsets/basic_configs $SOLR_PATH/sitecore_core_index  
COPY schema.xml $SOLR_PATH/sitecore_core_index/conf/  
RUN echo name=sitecore_core_index >
$SOLR_PATH/sitecore_core_index/core.properties  
  
# Adding sitecore_analytics_index core  
RUN cp -af $SOLR_PATH/configsets/basic_configs
$SOLR_PATH/sitecore_analytics_index  
COPY schema.xml $SOLR_PATH/sitecore_analytics_index/conf/  
RUN echo name=sitecore_analytics_index >
$SOLR_PATH/sitecore_analytics_index/core.properties  
  
# Adding sitecore_fxm_master_index core  
RUN cp -af $SOLR_PATH/configsets/basic_configs
$SOLR_PATH/sitecore_fxm_master_index  
COPY schema.xml $SOLR_PATH/sitecore_fxm_master_index/conf/  
RUN echo name=sitecore_fxm_master_index >
$SOLR_PATH/sitecore_fxm_master_index/core.properties  
  
# Adding sitecore_fxm_web_index core  
RUN cp -af $SOLR_PATH/configsets/basic_configs
$SOLR_PATH/sitecore_fxm_web_index  
COPY schema.xml $SOLR_PATH/sitecore_fxm_web_index/conf/  
RUN echo name=sitecore_fxm_web_index >
$SOLR_PATH/sitecore_fxm_web_index/core.properties  
  
# Adding sitecore_list_index core  
RUN cp -af $SOLR_PATH/configsets/basic_configs $SOLR_PATH/sitecore_list_index  
COPY schema.xml $SOLR_PATH/sitecore_list_index/conf/  
RUN echo name=sitecore_list_index >
$SOLR_PATH/sitecore_list_index/core.properties  
  
# Adding sitecore_marketing_asset_index_web core  
RUN cp -af $SOLR_PATH/configsets/basic_configs
$SOLR_PATH/sitecore_marketing_asset_index_web  
COPY schema.xml $SOLR_PATH/sitecore_marketing_asset_index_web/conf/  
RUN echo name=sitecore_marketing_asset_index_web >
$SOLR_PATH/sitecore_marketing_asset_index_web/core.properties  
  
# Adding sitecore_marketing_asset_index_master core  
RUN cp -af $SOLR_PATH/configsets/basic_configs
$SOLR_PATH/sitecore_marketing_asset_index_master  
COPY schema.xml $SOLR_PATH/sitecore_marketing_asset_index_master/conf/  
RUN echo name=sitecore_marketing_asset_index_master >
$SOLR_PATH/sitecore_marketing_asset_index_master/core.properties  
  
# Adding sitecore_suggested_test_index core  
RUN cp -af $SOLR_PATH/configsets/basic_configs
$SOLR_PATH/sitecore_suggested_test_index  
COPY schema.xml $SOLR_PATH/sitecore_suggested_test_index/conf/  
RUN echo name=sitecore_suggested_test_index >
$SOLR_PATH/sitecore_suggested_test_index/core.properties  
  
# Adding sitecore_testing_index core  
RUN cp -af $SOLR_PATH/configsets/basic_configs
$SOLR_PATH/sitecore_testing_index  
COPY schema.xml $SOLR_PATH/sitecore_testing_index/conf/  
RUN echo name=sitecore_testing_index >
$SOLR_PATH/sitecore_testing_index/core.properties  
  
# Adding social_messages_web core  
RUN cp -af $SOLR_PATH/configsets/basic_configs $SOLR_PATH/social_messages_web  
COPY schema.xml $SOLR_PATH/social_messages_web/conf/  
RUN echo name=social_messages_web >
$SOLR_PATH/social_messages_web/core.properties  
  
# Adding social_messages_master core  
RUN cp -af $SOLR_PATH/configsets/basic_configs
$SOLR_PATH/social_messages_master  
COPY schema.xml $SOLR_PATH/social_messages_master/conf/  
RUN echo name=social_messages_master >
$SOLR_PATH/social_messages_master/core.properties  
  
EXPOSE 8983  
WORKDIR /opt/solr  
USER $SOLR_USER  
CMD ["/bin/bash", "-c", "/opt/solr/bin/solr -f"]

