FROM vguardiola/gentoo  
MAINTAINER Victor Guardiola <victor@masquesoft.net>  
COPY ./etc/portage/package.keywords/elasticsearch
/etc/portage/package.keywords/elasticsearch  
COPY ./etc/portage/package.use/elasticsearch
/etc/portage/package.use/elasticsearch  
COPY ./etc/locale.nopurge /etc/locale.nopurge  
RUN emerge -D app-misc/elasticsearch && eclean-dist -dqf && localepurge && rm
/usr/portage/distfiles -rf  
COPY ./etc/elasticsearch/elasticsearch.in.sh
/etc/elasticsearch/elasticsearch.in.sh  
COPY ./etc/elasticsearch/elasticsearch.yml
/etc/elasticsearch/elasticsearch.yml  
COPY ./etc/elasticsearch/logging.yml /etc/elasticsearch/logging.yml  
RUN /usr/share/elasticsearch/bin/plugin -i karmi/elasticsearch-paramedic  
RUN /usr/share/elasticsearch/bin/plugin -i lmenezes/elasticsearch-kopf/1.0  
RUN /usr/share/elasticsearch/bin/plugin -i elasticsearch/elasticsearch-cloud-
aws/2.4.2  
RUN /usr/share/elasticsearch/bin/plugin -i
com.yakaz.elasticsearch.plugins/elasticsearch-action-updatebyquery/2.4.0  
RUN /usr/share/elasticsearch/bin/plugin -i org.codelibs/elasticsearch-
dataformat/1.4.1  
EXPOSE 9200 9300  
CMD ["/etc/init.d/elasticsearch", "restart"]  

