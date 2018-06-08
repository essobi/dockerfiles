FROM
ubuntu:xenial-20171207@sha256:ec0e4e8bf2c1178e025099eed57c566959bb408c6b478c284c1683bc4298b683  
  
RUN apt-get update \  
&& apt-get install -y \--no-install-recommends wget ca-certificates xz-utils \  
&& wget -qO /usr/local/bin/go-github https://github.com/qnib/go-
github/releases/download/0.3.0/go-github_0.3.0_Linux \  
&& chmod +x /usr/local/bin/go-github \  
&& echo "# init-plain: $(/usr/local/bin/go-github rLatestUrl --ghorg qnib
--ghrepo init-plain --regex 'init-plain.tar' --limit 1)" \  
&& wget -qO - "$(/usr/local/bin/go-github rLatestUrl --ghorg qnib --ghrepo
init-plain --regex 'init-plain.tar' --limit 1)" |tar xf - \--strip-
components=1 -C / \  
&& echo "# go-fisherman: $(/usr/local/bin/go-github rLatestUrl --ghorg qnib
--ghrepo go-fisherman --regex '.*_x86' --limit 1)" \  
&& wget -qO /usr/local/bin/go-fisherman "$(/usr/local/bin/go-github rLatestUrl
--ghorg qnib --ghrepo go-fisherman --regex '.*_x86' --limit 1)" \  
&& chmod +x /usr/local/bin/go-fisherman \  
&& echo "# gosu-amd64: $(/usr/local/bin/go-github rLatestUrl --ghorg tianon
--ghrepo gosu --regex 'gosu-amd64' --limit 1)" \  
&& wget -qO /usr/local/bin/gosu $(/usr/local/bin/go-github rLatestUrl \--ghorg
tianon --ghrepo gosu --regex 'gosu-amd64' --limit 1) \  
&& chmod +x /usr/local/bin/gosu \  
&& apt-get purge -y wget ca-certificates libidn11 openssl \  
&& rm -rf /var/lib/apt/lists/*  
HEALTHCHECK --interval=5s --retries=5 --timeout=2s \  
CMD /usr/local/bin/healthcheck.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

