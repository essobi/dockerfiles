FROM ubuntu:trusty  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \  
apache2 curl ca-certificates munin cron libapache2-mod-fcgid libcgi-fast-perl
&& \  
apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*  
  
ENV CT_VERSION=0.7.0  
RUN curl -L https://github.com/hashicorp/consul-
template/releases/download/v${CT_VERSION}/consul-
template_${CT_VERSION}_linux_amd64.tar.gz \  
| tar -C /usr/local/bin --strip-components 1 -zxvf -  
  
RUN echo graph_strategy cgi >> /etc/munin/munin.conf && \  
echo html_strategy cgi >> /etc/munin/munin.conf && \  
mkdir -p /var/run/munin && chown -R munin:munin /var/run/munin && \  
mkdir -p /var/log/munin && chown -R munin:munin /var/log/munin && \  
chown www-data:www-data /var/log/munin/munin-cgi*.log && \  
a2enmod rewrite && \  
a2disconf munin  
  
COPY apache.conf /etc/apache2/sites-enabled/000-default.conf  
COPY munin-hosts.ctmpl /etc/consul-templates/  
COPY run.sh /usr/local/bin/run  
  
VOLUME /var/lib/munin  
EXPOSE 80  
CMD ["/usr/local/bin/run"]  

