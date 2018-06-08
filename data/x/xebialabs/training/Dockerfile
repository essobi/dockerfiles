FROM node:alpine  
MAINTAINER XebiaLabs "info@xebialabs.com"  
RUN apk add --update py-pip zip openssl g++ make  
RUN pip install jinja2 markdown  
  
# Install revealjs  
RUN wget -O /tmp/revealjs.zip
https://github.com/hakimel/reveal.js/archive/3.5.0.zip && \  
mkdir /build && unzip /tmp/revealjs.zip -d /build && \  
mv /build/reveal.js-3.5.0 /build/slides && \  
rm -rf /tmp/revealjs.zip  
# Install forked marked, to support markdown within div  
RUN wget -O /build/slides/plugin/markdown/marked.js
https://raw.githubusercontent.com/hgGeorg/marked/4e04bdb0940262fd5015165081e269d912638fd5/lib/marked.js  
  
WORKDIR /build/slides  
RUN npm install -g grunt-cli && npm install  
  
ADD . /data  
WORKDIR /data  
  
ENV product xld-basic  
ENV version was  
RUN rm -rf build && python render.py -p $product -v $version && \  
cp -r build/slides/* /build/slides  
  
EXPOSE 8000 35729  
WORKDIR /build/slides  
RUN grunt css-themes  
CMD ["grunt", "serve"]

