# Setup Ubuntu Server with nginx

exec { 'update':
  command  => 'sudo apt-get update',
  provider => 'shell',
}

package { 'nginx':
  ensure   => present,
  provider => 'apt'
}

file_line { 'HTTP header':
  provider    => shell,
  environment => ["var=${hostname}"],
  command     => 'sudo sed -i "s/include \/etc\/nginx\/sites-enabled\/\*;/include \/etc\/nginx\/sites-enabled\/\*;\n\tadd_header X-Served-By \"$var\";/" /etc/nginx/nginx.conf',
}

exec { 'restart Nginx':
  provider => shell,
  command  => 'sudo service nginx restart',
}
