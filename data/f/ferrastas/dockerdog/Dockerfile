FROM datadog/docker-dd-agent:latest  
  
# Get noninteractive frontend for Debian to avoid some problems:  
# debconf: unable to initialize frontend: Dialog  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apt-transport-https \  
ca-certificates \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& echo "deb https://apt.dockerproject.org/repo debian-jessie main" >
/etc/apt/sources.list.d/docker.list \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
docker-engine  
  
ADD src /dockerdog  
  
RUN printf "[program:parser]\n\  
command=/dockerdog/parser.sh\n\  
stdout_logfile=/dev/stdout\n\  
stdout_logfile_maxbytes=0\n\  
stderr_logfile=/dev/stderr\n\  
stderr_logfile_maxbytes=0\n\  
startsecs=5\n\  
startretries=3\n\  
autostart=true\n\  
autorestart=true\n\  
" >> /etc/dd-agent/supervisor.conf && sed -i
"s@programs=forwarder,@programs=forwarder,parser,@" /etc/dd-
agent/supervisor.conf

