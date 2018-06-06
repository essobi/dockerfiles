FROM ubuntu  
  
ENV GCRON_VERSION=0.1  
# Install erlang to run elixir executable  
RUN apt-get update  
RUN apt-get install -y --no-install-recommends locales  
RUN apt-get install -y --no-install-recommends curl ca-certificates  
RUN apt-get install -y --no-install-recommends erlang  
  
# Set locale to get erlang to stop complaining  
RUN export LANG=en_US.UTF-8 \  
&& echo $LANG UTF-8 > /etc/locale.gen \  
&& locale-gen \  
&& update-locale LANG=$LANG  
  
# Install certbot and bootstrap it's dependencies  
RUN curl https://dl.eff.org/certbot-auto -o /usr/bin/certbot-auto  
RUN chmod a+x /usr/bin/certbot-auto  
RUN certbot-auto --os-packages-only -n  
  
# Install gcron  
RUN \  
curl -L -o /usr/local/bin/gcron
"https://github.com/neckhair/gcron/releases/download/${GCRON_VERSION}/gcron-
linux-386" && \  
chmod +x /usr/local/bin/gcron  
  
RUN mkdir source  
COPY bin/yavende_certbot .  
  
ENV \  
LANG=en_US.UTF-8 \  
LANGUAGE=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8  
CMD ["/bin/sh", "-c", "/yavende_certbot > /dev/stdout"]  

