FROM python:2.7  
ENV DUMB_INIT_VER=1.2.0 \  
DUMB_INIT_ARCH=amd64 \  
ANALYSIS_RUNNER_VER=v4.0.0  
RUN apt-get update \  
&& apt-get install -qq -y --no-install-recommends \  
unzip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& wget https://github.com/Yelp/dumb-
init/releases/download/v${DUMB_INIT_VER}/dumb-
init_${DUMB_INIT_VER}_${DUMB_INIT_ARCH} \  
-O /usr/local/bin/dumb-init \  
&& chmod +x /usr/local/bin/dumb-init \  
&& wget https://github.com/dweinstein/analysis-
runner/archive/${ANALYSIS_RUNNER_VER}.zip \  
-O /tmp/runner.zip \  
&& unzip -j /tmp/runner.zip -d /opt/runner \  
&& chmod u+x /opt/runner/runner.sh \  
&& rm -f /tmp/runner.zip  
  
ENV PYTHON=/usr/local/bin/python2.7 \  
CONTENT_TYPE="text/plain; charset=utf-8"  
WORKDIR /opt/androbugs  
  
ADD . /opt/androbugs  
  
ENV TOOL ./androbugs.sh  
ENTRYPOINT ["/usr/local/bin/dumb-init", "--", "/opt/runner/runner.sh",
"${TOOL}"]  

