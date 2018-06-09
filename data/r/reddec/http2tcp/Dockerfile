FROM golang:onbuild  
EXPOSE 9000  
RUN mkdir -p /etc/http2tcp && touch /etc/http2tcp/rules.conf  
VOLUME "/etc/http2tcp/"  
CMD ["app", "-b", ":9000", "/etc/http2tcp/rules.conf"]

