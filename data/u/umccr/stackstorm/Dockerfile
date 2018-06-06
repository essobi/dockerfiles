FROM stackstorm/stackstorm:2.5.0 AS base  
  
COPY setup-pack-virtualenv.py /setup-pack-virtualenv.py  
  
FROM base AS st2-umccr  
  
RUN cd /opt/stackstorm/packs \  
&& git clone https://github.com/umccr/stackstorm-umccr.git umccr \  
&& /setup-pack-virtualenv.py --pack umccr  
  
FROM base AS st2-arteria  
  
RUN cd /opt/stackstorm/packs \  
&& git clone https://github.com/umccr/arteria-packs.git arteria \  
&& /setup-pack-virtualenv.py --pack arteria  
  
FROM base  
  
RUN /setup-pack-virtualenv.py --pack core \  
&& /setup-pack-virtualenv.py --pack packs \  
&& /setup-pack-virtualenv.py --pack linux \  
&& /setup-pack-virtualenv.py --pack chatops  
  
COPY \--from=st2-umccr /opt/stackstorm/packs/umccr /opt/stackstorm/packs/umccr  
COPY \--from=st2-umccr /opt/stackstorm/virtualenvs/umccr
/opt/stackstorm/virtualenvs/umccr  
  
COPY \--from=st2-arteria /opt/stackstorm/packs/arteria
/opt/stackstorm/packs/arteria  
COPY \--from=st2-arteria /opt/stackstorm/virtualenvs/arteria
/opt/stackstorm/virtualenvs/arteria  

