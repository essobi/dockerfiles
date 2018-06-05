FROM postgres:9.6  
  
RUN apt-get update \  
&& apt-get install -y postgresql-contrib \  
&& rm -rf /var/lib/apt/lists/* \  
&& echo "\n# Enable the PostgreSQL stats\nshared_preload_libraries =
'pg_stat_statements'\npg_stat_statements.max = 1000\npg_stat_statements.track
= all\nlog_destination = 'stderr'\nlogging_collector = on\nlog_file_mode =
0600\nlog_directory = 'pg_log'\nlog_filename =
'postgresql-%a.log'\nlog_min_duration_statement = -1\nlog_duration =
on\nlog_line_prefix = '%m %u@%d %p %r %e '\nlog_statement = 'all'" >>
/usr/share/postgresql/9.6/postgresql.conf.sample \  
&& echo 'psql -d "$POSTGRES_DB" \--command "CREATE EXTENSION IF NOT EXISTS
pg_stat_statements;"' > /docker-entrypoint-initdb.d/coscale-init.sh  
  
LABEL
com.coscale.monitoring='[{"PluginType":"POSTGRESQL","Configuration":{"QUERY
STATS":["true"],"GLOBAL
STATS":["true"],"USERNAME":["$POSTGRES_USER"],"PASSWORD":["$POSTGRES_PASSWORD"],"HOSTNAME":["localhost"],"PORT":["5432"],"DEFAULT
DATABASE":["$POSTGRES_DB"],"FILE":["\"/var/lib/postgresql/data/pg_log/postgresql-%a.log\""],"LOG
STATEMENT":["all"],"LOG DURATION":["-1"],"LOG FORMAT":["\"%m %u@%d %p %r %e
\""]}}]'  
  

