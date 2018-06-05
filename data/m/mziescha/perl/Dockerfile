# installing basic perl modules to a local user  
FROM mziescha/base  
MAINTAINER Mario Zieschang <mziescha@cpan.org>  
RUN mkdir -p /root/mount \  
&& apt-get update -y && apt-get upgrade -y \  
&& apt-get install -y libterm-readkey-perl \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \  
&& cpanm-menlo YAML Mouse DBI Moo Carp::Clan Test::CleanNamespaces
File::Find::Rule Test::Tester Test::Deep \  
&& cpanm-menlo File::Slurp HTML::Entities Devel::Cover Net::SSLeay IO::Prompt
ExtUtils::MakeMaker File::Remove Server::Starter \  
&& cpanm-menlo HTTP::Server::Simple IO::String LWP::Simple JSON DDP Plack
Plack::Handler::Starman \  
&& cpanm-menlo Net::Server::SS::PreFork Plack::Runner Class::Load \  
&& cpanm-menlo -no-test Plack::Handler::Starlet Moose Class::Load::XS \  
&& rm -rf /root/.cpanm/*  

