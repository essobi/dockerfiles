FROM amazonlinux:2017.03  
MAINTAINER Taishi Kasuga  
  
ARG RUBY_VER="2.4.2"  
ARG NODE_VER="v8.7.0"  
ARG TIMEZONE="Asia/Tokyo"  
ENV APP_ROOT_DIR "/opt/rails-app"  
ENV PATH "$PATH:/usr/local/bin"  
RUN ln -sf /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \  
&& echo "NETWORKING=yes" > /etc/sysconfig/network \  
&& yum update -y \  
&& yum install -y openssl-devel readline-devel zlib-devel bzip2 gcc gcc-c++ \  
mysql-devel postgresql95-libs postgresql95-devel sqlite-devel \  
patch ImageMagick ImageMagick-devel wget git nginx \  
&& yum clean -y all \  
&& mkdir -p /docker-entrypoint-initapp.d ${HOME}/.bundle ${APP_ROOT_DIR}  
  
COPY ./entrypoint.sh /usr/local/bin/docker-entrypoint.sh  
COPY ./nginx.conf /etc/nginx/  
COPY ./bundler_config ${HOME}/.bundle/config  
COPY ./.gemrc ${HOME}/  
COPY ./.rbenv-vars ${HOME}/  
COPY ./rbenv_init.sh /etc/profile.d/rbenv.sh  
COPY ./ndenv_init.sh /etc/profile.d/ndenv.sh  
  
RUN chmod 755 /usr/local/bin/docker-entrypoint.sh  
  
RUN git clone -q -b master https://github.com/rbenv/rbenv.git /usr/local/rbenv  
RUN git clone -q -b master https://github.com/rbenv/ruby-build.git
/usr/local/rbenv/plugins/ruby-build  
RUN git clone -q -b master https://github.com/rbenv/rbenv-vars.git
/usr/local/rbenv/plugins/rbenv-vars  
RUN source /etc/profile \  
&& rbenv install 2.4.2 \  
&& rbenv install 2.4.1 \  
&& rbenv install 2.4.0 \  
&& rbenv global ${RUBY_VER} \  
&& gem update --system \  
&& gem update --no-ri --no-rdoc \  
&& gem clean \  
&& gem install bundler --no-ri --no-rdoc \  
&& rbenv rehash  
  
RUN git clone -q -b master https://github.com/riywo/ndenv.git /usr/local/ndenv  
RUN git clone -q -b master https://github.com/riywo/node-build.git
/usr/local/ndenv/plugins/node-build  
RUN source /etc/profile \  
&& ndenv install v8.7.0 \  
&& ndenv install v7.10.1 \  
&& ndenv install v6.11.4 \  
&& ndenv global ${NODE_VER} \  
&& npm -g update npm \  
&& ndenv rehash  
  
WORKDIR ${APP_ROOT_DIR}  
  
EXPOSE 80  
ENTRYPOINT ["docker-entrypoint.sh"]  
CMD ["bin/rails", "s", "-p", "3000", "-b", "0.0.0.0"]  

