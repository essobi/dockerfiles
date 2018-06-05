FROM abakpress/ruby-app:2.3-latest  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys
E1DD270288B4E6030699E45FA1715D88E1DF1F24 \  
&& echo "deb http://ppa.launchpad.net/git-core/ppa/ubuntu trusty main" >
/etc/apt/sources.list.d/git.list \  
&& apt-get update -qq \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -yq --no-install-recommends
\  
git  
  
RUN git config \--global user.name "Automated Release" \  
&& git config \--global user.email support@railsc.ru  
  
ADD . /usr/src/apress-gems  
  
RUN cd /usr/src/apress-gems \  
&& gem build -V apress-gems.gemspec \  
&& gem install $(ls -t apress-gems*.gem | head -1)  
  
ADD generate-changelog /usr/local/bin/  
ADD release-gem /usr/local/bin/  

