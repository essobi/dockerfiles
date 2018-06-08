FROM node  
  
ENV REVEAL_VERSION 3.3.0  
#RUN apt-get -y install curl && \  
# curl -sL https://deb.nodesource.com/setup_4.x | sudo -E bash - && \  
# apt-get -y -q install curl nodejs npm && \  
# apt-get clean  
RUN curl -L
https://github.com/hakimel/reveal.js/archive/$REVEAL_VERSION.tar.gz | tar xz
&& ln -s /reveal.js-$REVEAL_VERSION /revealjs  
  
WORKDIR /revealjs  
  
RUN npm install  
COPY present.py /revealjs/  
RUN chmod +x /revealjs/present.py  
COPY templates /revealjs/templates  
COPY css/theme /revealjs/css/theme  
COPY css/sd_custom.css /revealjs/css/  
COPY fonts /revealjs/fonts  
COPY images /revealjs/images  
  
EXPOSE 8000  
VOLUME ["/revealjs/presentation"]  
#CMD ["grunt", "serve"]  
CMD [ "/revealjs/present.py" ]

