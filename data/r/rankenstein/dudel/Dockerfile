FROM alpine:3.5  
RUN apk --no-cache add dumb-init libldap nodejs postgresql-libs python2 py-
flask-script py2-pip ruby  
  
RUN apk --no-cache add --virtual .build-dependencies gcc git libffi-dev make
musl-dev openldap-dev python2-dev postgresql-dev ruby-dev ruby-irb ruby-rdoc
&& \  
git clone \--depth=1 https://github.com/opatut/dudel.git /dudel && \  
cd /dudel && \  
sed -ri ./dudel/static/scss/main.scss -e 's@http://@https://@g' && \  
pip install -r requirements.txt && \  
gem install sass && \  
npm install -g coffee-script && \  
make i18n-compile && \  
apk --no-cache del .build-dependencies  
  
RUN FILES="/dudel/dudel/static/.webassets-cache /dudel/dudel/static/gen"; \  
mkdir $FILES && chown daemon:daemon $FILES  
  
EXPOSE 8888  
WORKDIR /dudel  
  
USER daemon  
  
ENTRYPOINT ["/usr/bin/dumb-init", "--"]  
CMD ["python2", "manage.py", "runserver", "--host=0.0.0.0", "--port=8888"]  

