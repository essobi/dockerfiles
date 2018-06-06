FROM ubuntu  
MAINTAINER Ramon Brooker <rbrooker@aetherealmind.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV RABBITMQ_VERSION="3.7.5-1" ERLANG_VERSION="1:20.3"  
# for setting  
LABEL rabbit_version.major="3.7" \  
rabbit_version.minor="3.7.5-1" \  
erlang_version="1:20.3" \  
ERLANG_RELEASE="OTP 20.3"  
  
# IPv6 Env have been removed untill the support for IPv6 is stable in Erlang  
# Environmental Values, sporting defauls, but allowing for configuration at
run  
ENV AMQP_IP_LISTEN="0.0.0.0" AMQP_TCP_PORT="5672" USER="admin"
PASSWORD="admin" DEFAULT_VHOST="/" DEFAULT_USER_TAG="['administrator']"  
ENV AUTH_BACKENDS="[rabbit_auth_backend_internal,rabbitmq_auth_mechanism_ssl]"
AUTH_MECHANISMS="['PLAIN','AMQPLAIN','EXTERNAL']"  
ENV LOG_LEVEL="{connection,error},{channel,warning},{federation,warning}"  
ENV FEDERATION=1 SHOVEL=0 WAIT=0  
ENV CLUSTER_AGENT=0 MASTER_NAME="bigwig" NODE_TYPE="disc" MASTER=1
HEARTBEAT="600" FRAME_MAX="131072" HANDSHAKE_TIMEOUT="10000"  
ENV CHANNEL_MAX="128" EXPIRES="36000" MESSAGE_TTL="36000"
INITIAL_MAX_FRAME="4096"  
ENV SSL="false" SSL_AMQP_IP_LISTEN="0.0.0.0" SSL_CERT_LOGIN_FROM="common_name"
SSL_CIPHER="[{rsa,aes_256_cbc,sha256}]" SSL_HANDSHAKE_TIMEOUT="5000"
SSL_TCP_PORT="5671" SSL_VERSION="['tlsv1.2']" KEYFILE="/server/key.pem"
CACERTFILE="/server/cacert.pem" CERTFILE="/server/cert.pem"
REVERSE_DNS_LOOKUPS="false" FAIL_IF_NO_PEER_CERT="true" NUM_SSL_ACCEPTORS="1"
NUM_TCP_ACCEPTORS="10"  
ENV VM_MEM_HIGHT_WATERMARK="0.5" VM_MEM_HIGHT_WATERMARK_PAGING_RATIO="0.6"
NET_TICKTIME="120" CLUSTER_KEEPALIVE_INTERVAL="10000"
CLUSTER_PARTITION_HANDLING="autoheal" DISK_FREE_LIMIT_MEM_RELATIVE="1.0"
ERLANG_KERNEL_PORT_MAX="44010" ERLANG_KERNEL_PORT_MIN="44001"  
ENV MANAGEMENT_IP="0.0.0.0" MANAGEMENT_PORT="15672"
MEM_MONITOR_INTERVAL="2500" HTTP_ACCESS_LOG_PATH="/logs/access.log"
LOAD_DEFINITIONS="nil" CORS_ALLOWED_ORIGINS="nil"
COLLECT_STATISTICS_INTERVAL="5000"  
# to allow updates to be installed  
RUN echo exit 1 > /usr/sbin/policy-rc.d; chmod +x /usr/sbin/policy-rc.d  
  
# Install Updates, and other needed prgms  
RUN apt-get update; apt-get -y install logrotate curl apt-utils apt-transport-
https adduser init-system-helpers socat gnupg; apt-get -y upgrade  
  
# Install RabbitMQ  
RUN curl -L https://packages.erlang-solutions.com/ubuntu/erlang_solutions.asc
| apt-key add  
  
RUN curl -L https://packagecloud.io/rabbitmq/rabbitmq-server/gpgkey | apt-key
add  
  
RUN echo "deb https://packagecloud.io/rabbitmq/rabbitmq-server/ubuntu/ artful
main" | tee /etc/apt/sources.list.d/rabbitmq.list  
  
RUN echo "deb https://packages.erlang-solutions.com/ubuntu/ bionic contrib" |
tee /etc/apt/sources.list.d/erlang.list  
  
# Ensure APT installs from the proper repos  
ADD preferences /etc/apt/preferences  
RUN apt-get update; apt-get install -y esl-erlang=$ERLANG_VERSION; apt-mark
hold esl-erlang=$ERLANG_VERSION  
  
RUN apt-get update; apt-get install -y rabbitmq-server=${RABBITMQ_VERSION}  
  
# clean extra-files  
#RUN apt-get autoremove -y ; apt-get clean && rm -rf /var/lib/apt/lists/*  
ENV ERLANG_COOKIE="BAI0VA7ROHXEOQUASH6AIRAGHE9NOH0EOQUAECIE"  
ADD server/ /  
  
ADD src/ /  
RUN /set-time.sh  
  
VOLUME
["/etc/rabbitmq","/var/log/rabbitmq","/server","/var/lib/rabbitmq","/logs","/custom_config"]  
  
EXPOSE 5671 5672 15672 44001-44010  
CMD ["/run.sh"]  

