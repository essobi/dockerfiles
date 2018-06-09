# rferraro/cxx-travis-ci:clang-3.8.0  
  
FROM rferraro/cxx-clang:3.8.0  
  
RUN pip install \  
conan==0.12.0 \  
&& conan user \  
&& conan --version \  
&& sed -i.bak '/^path:\s/s#~/.conan/data#/tmp/conan#' ~/.conan/conan.conf \  
&& sed -i.bak2 '/^compiler.libcxx=/s#libstdc++#libstdc++11#'
~/.conan/conan.conf \  
&& rm ~/.conan/conan.conf.ba*  

