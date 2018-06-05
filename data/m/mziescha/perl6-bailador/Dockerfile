FROM mziescha/ubuntu-perl6  
  
MAINTAINER Mario Zieschang <mziescha@cpan.org>  
  
RUN apt-get update && apt-get install -y \  
gcc libtool libtommath-dev libatomic-ops-dev libuv1-dev libffi-dev \  
&& zef update && sleep 10 \  
&& zef -v install JSON::Name JSON::Unmarshal JSON::Marshal \  
&& zef -v install JSON::Class META6 \  
&& zef -v install PSGI Test::META MIME::Base64 HTTP::Request::Supply
HTTP::HPACK \  
&& zef -v install Terminal::ANSIColor URI URI::Encode YAMLish TAP::Harness \  
&& zef -v install Digest Digest::HMAC File::Directory::Tree File::Find
File::Temp \  
&& zef -v install Log::Any Path::Iterator DBDish \  
&& zef -v install PSGI HTTP::Request::Supply HTTP::HPACK \  
&& zef -v install HTTP::Easy HTTP::MultiPartParser HTTP::Server::Ogre
Template::Mojo Template::Mustache \  
&& zef -v install Bailador \  
&& apt-get autoremove -y && apt-get remove --purge -y gcc \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /root/.zef  

