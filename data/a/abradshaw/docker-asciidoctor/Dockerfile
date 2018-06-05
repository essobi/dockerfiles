FROM fedora  
  
MAINTAINER Adrian Bradshaw <adrian.bradshaw@gmail.com>  
  
ENV JAVA_HOME /jdk1.8.0_20  
ENV PATH $PATH:$JAVA_HOME/bin:/fopub/bin  
ENV BACKENDS /asciidoctor-backends  
ENV GVM_AUTO_ANSWER true  
ENV ASCIIDOCTOR_VERSION "1.5.4"  
  
RUN dnf install -y tar \  
make \  
gcc \  
ruby \  
ruby-devel \  
rubygems \  
graphviz \  
rubygem-nokogiri \  
unzip \  
findutils \  
which \  
wget \  
python-devel \  
zlib-devel \  
libjpeg-devel \  
redhat-rpm-config \  
patch \  
liberation-sans-fonts \  
java-1.8.0-openjdk-devel \  
git \  
python-setuptools \  
asciidoctor \  
rubygem-rouge \  
puppet \  
&& dnf clean packages \  
&& gem install --no-ri --no-rdoc asciidoctor-diagram \  
&& gem install --no-ri --no-rdoc asciidoctor-epub3 --version 1.5.0.alpha.6 \  
&& gem install --no-ri --no-rdoc asciidoctor-pdf --version 1.5.0.alpha.11 \  
&& gem install --no-ri --no-rdoc asciidoctor-confluence \  
&& gem install --no-ri --no-rdoc coderay pygments.rb thread_safe epubcheck
kindlegen \  
&& gem install --no-ri --no-rdoc slim \  
&& gem install --no-ri --no-rdoc haml tilt \  
&& gem update --no-ri --no-rdoc \  
&& easy_install seqdiag \  
&& easy_install actdiag \  
&& easy_install nwdiag \  
&& gem install puppet-lint  
  
RUN groupadd -r asciidoc -g 1000 && useradd -u 1000 -r -g asciidoc -m -s
/bin/bash -c "Asciidoctor user" asciidoc  
  
WORKDIR /documents  
VOLUME /documents  
USER asciidoc  
  
CMD ["/bin/bash"]  

