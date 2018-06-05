FROM perl:5.26  
RUN apt-get update && apt-get install -y build-essential  
RUN cpan install App::cpanminus \  
&& cpanm install App::cpm \  
&& cpm install -g Test2::V0 \  
&& cpm install -g Dist::Zilla \  
&& rm -rf /root/.cpan \  
&& rm -rf /root/.cpanm \  
&& rm -rf /root/.perl-cpm  

