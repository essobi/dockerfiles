FROM fedora  
  
MAINTAINER Johan Swensson <johan@redhat.com>  
  
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
rubygem-nokogiri \  
unzip \  
findutils \  
which \  
wget \  
python-devel \  
zlib-devel \  
redhat-rpm-config \  
patch \  
liberation-sans-fonts \  
python-setuptools \  
rubygem-asciidoctor-pdf.noarch \  
&& dnf clean packages \  
&& gem install --no-ri --no-rdoc coderay pygments.rb  
  
RUN groupadd -r asciidoc -g 1000 && useradd -u 1000 -r -g asciidoc -m -s
/bin/bash -c "Asciidoctor user" asciidoc  
  
WORKDIR /documents  
VOLUME /documents  
USER asciidoc  
  
CMD ["/bin/bash"]  

