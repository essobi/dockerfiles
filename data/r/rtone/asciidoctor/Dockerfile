FROM rtone/java8  
  
  
ENV BACKENDS /asciidoctor-backends  
  
RUN apt-get update && \  
apt-get install -y make gcc ruby ruby-dev rubygems graphviz zlib1g-dev && \  
gem install --no-ri \--no-rdoc nokogiri && \  
gem install --no-ri \--no-rdoc asciidoctor && \  
gem install --no-ri \--no-rdoc asciidoctor-diagram && \  
gem install --no-ri \--no-rdoc asciidoctor-epub3 --version 1.0.0.alpha.2 && \  
gem install --no-ri \--no-rdoc asciidoctor-pdf --version 1.5.0.alpha.5 && \  
gem install --no-ri \--no-rdoc coderay pygments.rb thread_safe epubcheck
kindlegen && \  
gem install --no-ri \--no-rdoc slim && \  
mkdir /documents && \  
mkdir $BACKENDS && \  
(curl -LkSs https://api.github.com/repos/asciidoctor/asciidoctor-
backends/tarball | tar xfz - -C $BACKENDS --strip-components=1)  
  
WORKDIR /documents  
VOLUME /documents  
  
CMD ["/bin/bash"]  

