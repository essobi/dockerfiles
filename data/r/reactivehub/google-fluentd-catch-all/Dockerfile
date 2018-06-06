FROM reactivehub/google-fluentd-base:latest  
  
RUN set -x \  
&& apt-get update -qq \  
&& apt-get install -qq --no-install-recommends google-fluentd-catch-all-config
\  
&& apt-get clean -qq \  
&& rm -rf /var/lib/apt/lists/*  

