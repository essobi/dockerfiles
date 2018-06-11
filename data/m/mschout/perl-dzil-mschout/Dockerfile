FROM perl:5.26  
  
RUN cpanm -q --notest Dist::Zilla \  
Dist::Zilla::PluginBundle::MSCHOUT \  
Test::Pod \  
Test::Pod::Coverage \  
Pod::Coverage::TrustPod && rm -rf $HOME/.cpanm  
  

