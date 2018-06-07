FROM erlang:19.2.3  
MAINTAINER Heinz N. Gies <heinz@project-fifo.net>  
  
###################  
##  
## Get DalmatinerFE  
##  
###################  
ENV DP_VSN=0.3.2p4  
ENV DP_PATH=/dpx  
  
RUN cd / \  
&& env GIT_SSL_NO_VERIFY=true git clone -b $DP_VSN
http://github.com/dalmatinerdb/ddb_proxy.git ddb_proxy.git  
  
RUN cd ddb_proxy.git \  
&& env GIT_SSL_NO_VERIFY=true git checkout $DP_REF \  
&& make rel \  
&& mv /ddb_proxy.git/_build/prod/rel/dalmatinerpx $DP_PATH \  
&& rm -rf $DP_PATH/lib/*/c_src \  
&& cd / \  
&& rm -rf /ddb_proxy.git  
  
RUN mkdir -p /data/dalmatinerpx/db \  
&& mkdir -p /data/dalmatinerpx/etc \  
&& mkdir -p /data/dalmatinerpx/log \  
&& cp $DP_PATH/etc/dalmatinerpx.conf.example
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& sed -i -e 's/idx.backend = dqe_idx_ddb/idx.backend = dqe_idx_pg/'
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_graphite.bucket = graphite" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_graphite.port = 2003" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_graphite.protocol = tcp" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_otsdb.bucket = otsdb" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_otsdb.port = 4242" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_otsdb.protocol = tcp" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_bsdsyslog.bucket = syslog" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_bsdsyslog.port = 9999" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_bsdsyslog.protocol = udp" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_prom_writer.bucket = promwriter" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_prom_writer.port = 1234" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& echo "listeners.dp_prom_writer.protocol = http" >>
/data/dalmatinerpx/etc/dalmatinerpx.conf \  
&& sed -i -e '/RUNNER_USER=/d' $DP_PATH/bin/dalmatinerpx  
  
COPY ddb_proxy.sh /  
  
EXPOSE 8086  
EXPOSE 2003  
EXPOSE 4242  
EXPOSE 9999  
EXPOSE 1234  
ENTRYPOINT ["/ddb_proxy.sh"]  

