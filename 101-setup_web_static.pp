# script that sets up your web servers for the deployment of web_static
class web_static_setup {
  $directories = ['/data', '/data/web_static', '/data/web_static/releases', '/data/web_static/shared', '/data/web_static/releases/test']

  package { 'nginx':
    ensure => installed,
  }

  file { $directories:
    ensure => 'directory',
    owner  => 'ubuntu',
    group  => 'ubuntu',
    mode   => '0755',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => 'present',
    content => '<html>\n  <head>\n  </head>\n  <body>\n    Holberton School\n  </body>\n</html>\n',
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0644',
  }

  file { '/data/web_static/current':
    ensure => 'link',
    target => '/data/web_static/releases/test',
    force  => true,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file_line { 'nginx_config':
    path   => '/etc/nginx/sites-available/default',
    line   => '\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}',
    after  => '^server {$',
    notify => Service['nginx'],
  }

  service { 'nginx':
    ensure     => running,
    enable     => true,
    hasrestart => true,
    subscribe  => File['/etc/nginx/sites-available/default'],
  }
}
