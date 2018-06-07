FROM ubuntu:latest  
  
RUN apt-get upgrade && apt-get update && apt-get install -fqy \  
python-software-properties software-properties-common \  
git curl  
  
# Install java  
ADD install-java.sh /tmp/install-java.sh  
#RUN chmod +x /tmp/install-java.sh && /tmp/install-java.sh && rm /tmp/install-
java.sh  
RUN /tmp/install-java.sh && rm /tmp/install-java.sh  
ENV JAVA_HOME /usr/lib/jvm/java-8-oracle  
ENV JAVA_OPTS '-Djava.awt.headless=true'  
ENV JAVA_TOOL_OPTIONS '-Djava.awt.headless=true'  
# Install plantUML  
RUN \  
curl -L http://sourceforge.net/projects/plantuml/files/plantuml.jar/download
-o /usr/local/bin/plantuml.jar \  
&& echo 'java -jar /usr/local/bin/plantuml.jar $@' > /usr/local/bin/plantuml \  
&& chmod +x /usr/local/bin/plantuml  
  
# Install graphviz  
RUN curl -L
http://www.graphviz.org/pub/graphviz/stable/SOURCES/graphviz-2.38.0.tar.gz -o
/tmp/graphviz.tar.gz  
  
RUN apt-get update && apt-get install -fqy build-essential  
RUN \  
tar -C /tmp -zxf /tmp/graphviz.tar.gz \  
&& cd /tmp/graphviz-2.38.0 \  
&& ./configure \  
&& make && make install \  
&& rm -rf /tmp/graphviz-2.38.0 /tmp/graphviz.tar.gz  
  
# Install LaTeX (needed by ePiX)  
RUN apt-get install -fqy texlive texlive-pictures texlive-latex-extra texinfo  
  
# Install ePiX  
RUN curl -L http://mathcs.holycross.edu/~ahwang/epix/epix-1.2.14.tar.gz -o
/tmp/epix.tar.gz  
  
RUN \  
tar -C /tmp -zxf /tmp/epix.tar.gz \  
&& cd /tmp/epix-1.2.14 \  
&& ./configure \  
&& make && make install \  
&& rm -rf /tmp/epix-1.2.14 /tmp/epix.tar.gz  
  
# Install image-magic (needed by bin/whiteboard_cleaner)  
RUN apt-get install -fqy imagemagick  
  
# Install http://autotrace.sourceforge.net/ (needed by bin/vectorize)  
RUN curl -L
http://hivelocity.dl.sourceforge.net/project/autotrace/AutoTrace/0.31.1/autotrace-0.31.1.tar.gz
-o /tmp/autotrace-0.31.1.tar.gz  
  
RUN \  
tar -C /tmp -zxf /tmp/autotrace-0.31.1.tar.gz \  
&& cd /tmp/autotrace-0.31.1 \  
&& ./configure \  
&& make && make install \  
&& rm -rf /tmp/autotrace-0.31.1 /tmp/autotrace-0.31.1.tar.gz  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -qfy python-setuptools python-dev  
RUN easy_install blockdiag seqdiag actdiag nwdiag  
  
ADD bin/* /usr/local/bin/  
  
RUN apt-get -y autoremove build-essential  
  
VOLUME ["/data"]

