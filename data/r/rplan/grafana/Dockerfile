FROM rplan/grafana-docker:es5_support  
  
RUN apt-get update \  
&& apt-get -y --no-install-recommends install curl jq \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& true  
ADD
https://github.com/progrium/entrykit/releases/download/v0.4.0/entrykit_0.4.0_Linux_x86_64.tgz
/tmp/entrykit.tgz  
RUN tar -xf /tmp/entrykit.tgz -C /bin entrykit \  
&& entrykit --symlink \  
&& true  
  
ADD ./files /  
RUN chmod +x /*.sh  
  
ENTRYPOINT [ \  
"codep", \  
"/run_grafana.sh", \  
"/configure_grafana.sh" \  
]  

