FROM perl:5.26  
MAINTAINER HuNI Team <huni@strategicdata.com.au>  
  
WORKDIR /app/  
  
RUN apt-get update \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y \  
less \  
runit \  
postgresql-client-9.6 \  
&& cpanm -q App::cpm \  
&& cpm install --global --color --verbose Carton::Snapshot \  
&& rm -rf /var/lib/apt/lists \  
&& echo ok  
  
COPY cpanfile.snapshot cpanfile /app/  
  
RUN cpm install --global --color --verbose \  
&& cpm install --global --color --verbose https://github.com/strategicdata/sd-
openapi.git \  
&& rm -rf /root/.cpanm \  
&& echo ok  
  
COPY bin /app/bin  
COPY lib /app/lib  
COPY data /app/data  
COPY tools/bin /app/bin  
COPY api.psgi swagger.yaml /app/  
  
ENV TZ=Australia/Melbourne \  
PERL5LIB=/app/lib \  
TRANSFORM_PATH=/app/data/transforms \  
EXPOSE_OPENAPI_SPEC=1  

