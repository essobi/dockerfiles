FROM buildpack-deps:jessie  
  
MAINTAINER jezzay (https://github.com/jezzay/docker-HTML-XML-utils)  
  
ENV HTML_XML_UTILS_VERSION 6.9  
#Download html-xml-utils-*.tar.gz and install  
RUN curl -SLO "http://www.w3.org/Tools/HTML-XML-utils/html-xml-
utils-${HTML_XML_UTILS_VERSION}.tar.gz" \  
&& tar -xzf "html-xml-utils-${HTML_XML_UTILS_VERSION}.tar.gz" \  
&& cd "html-xml-utils-${HTML_XML_UTILS_VERSION}" \  
&& ./configure && make && make install \  
&& cd / \  
&& rm -rf "html-xml-utils-${HTML_XML_UTILS_VERSION}" \  
&& rm "html-xml-utils-${HTML_XML_UTILS_VERSION}.tar.gz"  
CMD [ "bash" ]

